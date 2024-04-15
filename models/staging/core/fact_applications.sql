{{
    config(
        materialized='table'
    )
}}

with applications as (
    select * from {{ ref('stg_staging_applications')}}
),
devices as (
    select * from {{ ref('stg_staging_devices')}}
),
dim_tenants as (
    select * from {{ ref("dim_tenants")}}
),
dim_agents as (
    select * from {{ ref("dim_agents")}}
)

select 
applications.*,
tenant.tenant_name,
device.device_name,
device.device_imei,

from applications

inner join dim_tenants as tenant
on applications.tenant_id = tenant.id

inner join dim_agents as agent 
on applications.agent_code = agent.agent_code

inner join devices as device 
on agent.device_id = device.id