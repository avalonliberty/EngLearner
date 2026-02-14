# Authentication

EngLearner uses Supabase Auth for user authentication.

## Flow

1. **Sign Up / Sign In**: Use Supabase Auth client (or dashboard)
2. **Get Token**: Receive JWT access token
3. **API Requests**: Include token in Authorization header

```
Authorization: Bearer <your-jwt-token>
```

## Protected Endpoints

All vocabulary endpoints require authentication. Include the JWT token in the request header.

## Token Refresh

Tokens expire after a set time. Use the refresh token to get a new access token.
