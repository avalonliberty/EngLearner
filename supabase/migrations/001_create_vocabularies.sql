-- Create vocabularies table for EngLearner
-- Run this in Supabase SQL Editor

-- Create the vocabularies table
CREATE TABLE IF NOT EXISTS public.vocabularies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    word TEXT NOT NULL,
    definition TEXT NOT NULL,
    example TEXT,
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    current_day_index INTEGER NOT NULL DEFAULT 0 CHECK (current_day_index >= 0 AND current_day_index <= 6),
    next_review_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL DEFAULT 'reviewing' CHECK (status IN ('pending', 'reviewing', 'completed')),
    streak_count INTEGER NOT NULL DEFAULT 0 CHECK (streak_count >= 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE public.vocabularies ENABLE ROW LEVEL SECURITY;

-- Create RLS policies

-- Users can only see their own vocabularies
CREATE POLICY "Users can only see own vocabularies"
    ON public.vocabularies FOR SELECT
    USING (auth.uid() = user_id);

-- Users can only insert their own vocabularies
CREATE POLICY "Users can only insert own vocabularies"
    ON public.vocabularies FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- Users can only update their own vocabularies
CREATE POLICY "Users can only update own vocabularies"
    ON public.vocabularies FOR UPDATE
    USING (auth.uid() = user_id);

-- Users can only delete their own vocabularies
CREATE POLICY "Users can only delete own vocabularies"
    ON public.vocabularies FOR DELETE
    USING (auth.uid() = user_id);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_vocabularies_user_id ON public.vocabularies(user_id);
CREATE INDEX IF NOT EXISTS idx_vocabularies_next_review_date ON public.vocabularies(next_review_date);
CREATE INDEX IF NOT EXISTS idx_vocabularies_user_review ON public.vocabularies(user_id, next_review_date);

-- Add updated_at trigger to automatically update the timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_vocabularies_updated_at
    BEFORE UPDATE ON public.vocabularies
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Enable auth for the table
COMMENT ON TABLE public.vocabularies IS 'Stores vocabulary items for spaced repetition learning';
