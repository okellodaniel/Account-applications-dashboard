with 

source as (

    select * from {{ source('staging', 'devices') }}

),

renamed as (

    select
        id,
        device_name,
        device_imei

    from source

)

select * from renamed
