---
title: Accessing configuration information
description: Accessing configuration information
keywords:
- NetAdapterCx accessing configuration information, NetCx accessing configuration information
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# Accessing configuration information

The NetAdapterCx class extension supports a set of functions that provide access to client driver registry parameters.

Typically, the client driver reads configuration info from its [*EVT_WDF_DRIVER_DEVICE_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function.

For a NetAdapter object, start by calling [**NetAdapterOpenConfiguration**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapteropenconfiguration) to get a handle to a configuration object.  You can then query it:

```C++
NETCONFIGURATION configuration;

status = NetAdapterOpenConfiguration(NetAdapter, 
                                     WDF_NO_OBJECT_ATTRIBUTES, 
                                     &configuration);
if (!NT_SUCCESS(status)) {
    return status;
}

status = NetConfigurationQueryUlong(configuration, 
                                    NET_CONFIGURATION_QUERY_ULONG_NO_FLAGS, 
                                    &SomeValue, 
                                    &myvalue);

NetConfigurationClose(configuration);
```

Opening and querying a configuration object for a net device is similar:

```C++
status = NetDeviceOpenConfiguration(Device, 
                                    WDF_NO_OBJECT_ATTRIBUTES, 
                                    &configuration);
if(!NT_SUCCESS(status))
{
    return status;
}

WDFCOLLECTION myStrings;

DECLARE_CONST_UNICODE_STRING(myValueName, L"ExampleValueName");

status = NetConfigurationQueryMultiString(configuration,
                                          myValueName,
                                          WDF_NO_OBJECT_ATTRIBUTES,
                                          myStrings);
```

There are `NetConfiguration*` functions for querying ULONG data, strings, multi-strings (similar to REG_MULTI_SZ), binary blobs, and software-configurable network addresses:

* [**NetConfigurationAssignBinary**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationassignbinary)
* [**NetConfigurationAssignMultiString**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationassignmultistring)
* [**NetConfigurationAssignUlong**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationassignulong)
* [**NetConfigurationAssignUnicodeString**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationassignunicodestring)
* [**NetConfigurationClose**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationclose)
* [**NetConfigurationOpenSubConfiguration**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationopensubconfiguration)
* [**NetConfigurationQueryBinary**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationquerybinary)
* [**NetConfigurationQueryMultiString**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationquerymultistring)
* [**NetConfigurationQueryLinkLayerAddress**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationquerylinklayeraddress)
* [**NetConfigurationQueryString**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationquerystring)
* [**NetConfigurationQueryUlong**](/windows-hardware/drivers/ddi/netconfiguration/nf-netconfiguration-netconfigurationqueryulong)
