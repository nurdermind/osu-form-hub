## RUN
```bash
    docker-compose up
```

## Endpoints
- Swagger - `/api/schema/swagger-ui/`
- Admin - `/api/admin/`
- Api-UI (Alternative for swagger) - `/api/`

## Default credentials for superuser
`admin:12345678`


## Cases

### Registration
POST `/api/auth/users/`

### JWT
- POST `/api/auth/jwt/create/` create a new tokens
- POST `/api/auth/jwt/refresh/` refresh access token by refresh token


All api auth-required requests must include Header:
`"Authorization": "Bearer *access-token*"` 