{{
    config(
        materialized='table'
    )
}}

select
    Id as id,
    TenantName as tenant_name,
from {{ ref('tenants_lookup') }}