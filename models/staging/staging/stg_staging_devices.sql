{{ 
    config(materialized="view") 
}}

with 

source as (
    select * from {{ source('staging', 'devices') }}
),

devices as (

    select
        id,
        device_name,
        device_imei

    from source

)

select * from devices
