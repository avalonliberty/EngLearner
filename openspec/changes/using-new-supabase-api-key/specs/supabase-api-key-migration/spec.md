## ADDED Requirements

### Requirement: Application initialization with new Supabase API keys
The application SHALL initialize the Supabase client using the new publishable and secret API keys instead of legacy JWT-based anon and service_role keys.

#### Scenario: Client initialization with publishable key
- **WHEN** application starts with `SUPABASE_PUBLISHABLE_KEY` environment variable set
- **THEN** Supabase client is initialized successfully
- **AND** client uses the new API key format (sb_publishable_...)

### Requirement: Environment variable configuration updates
All configuration files and documentation SHALL reference the new API key environment variable names. The application SHALL use only the new publishable and secret API keys.

#### Scenario: Update .env.example with new variable names
- **WHEN** developer reads .env.example file
- **THEN** file contains `SUPABASE_PUBLISHABLE_KEY` and `SUPABASE_SECRET_KEY` variables
- **AND** file describes new key format (sb_publishable_... and sb_secret_...)

### Requirement: Simplified authentication without JWT secret
The application SHALL remove dependency on `SUPABASE_JWT_SECRET` for authentication. The Supabase client SHALL handle authentication internally using the new API key system.

#### Scenario: Token verification without JWT secret
- **WHEN** user makes authenticated request with valid token
- **THEN** application verifies token using Supabase client
- **AND** no JWT secret is required for verification

### Requirement: Secret key usage for elevated privileges
Operations requiring elevated privileges (bypassing RLS) SHALL use `SUPABASE_SECRET_KEY` instead of service_role JWT key. The secret key MUST only be used in backend components.

#### Scenario: Admin operation with secret key
- **WHEN** application performs privileged operation on server
- **THEN** Supabase client initialized with `SUPABASE_SECRET_KEY`
- **AND** operation bypasses Row Level Security
- **AND** secret key is not exposed to client-side code

### Requirement: Documentation completeness
All documentation (SETUP.md, inline comments) SHALL reference the new API key system and provide setup instructions for new users.

#### Scenario: Updated setup guide
- **WHEN** developer reads SETUP.md
- **THEN** guide instructs to use publishable and secret keys
- **AND** guide includes steps to obtain new keys from Supabase dashboard