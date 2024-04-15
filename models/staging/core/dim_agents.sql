{{
    config(
        materialized='table'
    )
}}

select
    Id as id,
    TenantId as tenant_id,
    DeviceId as device_id,
    AgentCode as agent_code
from {{ ref('agents_lookup') }}