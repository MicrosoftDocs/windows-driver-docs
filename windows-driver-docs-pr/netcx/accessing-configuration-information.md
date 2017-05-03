---
title: Accessing Configuration Information
---

# Accessing Configuration Information

The NetAdapterCx class extension supports a set of functions that provide access to client driver registry parameters.

Typically, the client driver reads configuration info from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function.

Start by calling [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) to get a handle to a configuration object.  You can then query it:

```cpp
NETCONFIGURATION configuration;

status = NetAdapterOpenConfiguration(NetAdapter, WDF_NO_OBJECT_ATTRIBUTES, &configuration);
if (! NT_SUCCESS(status)) {
    return status;
}

status = NetConfigurationQueryUlong(configuration, NET_CONFIGURATION_QUERY_ULONG_NO_FLAGS, &SomeValue, &myvalue);

NetConfigurationClose(configuration);
```
There are `NetConfiguration*` functions for querying ULONG data, strings, multi-strings (similar to REG_MULTI_SZ), binary blobs, and software-configurable network addresses:

* [**NetConfigurationAssignBinary**](netconfigurationassignbinary.md)
* [**NetConfigurationAssignMultiString**](netconfigurationassignmultistring.md)
* [**NetConfigurationAssignUlong**](netconfigurationassignulong.md)
* [**NetConfigurationAssignUnicodeString**](netconfigurationassignunicodestring.md)
* [**NetConfigurationClose**](netconfigurationclose.md)
* [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md)
* [**NetConfigurationQueryBinary**](netconfigurationquerybinary.md)
* [**NetConfigurationQueryMultiString**](netconfigurationquerymultistring.md)
* [**NetConfigurationQueryNetworkAddress**](netconfigurationquerynetworkaddress.md)
* [**NetConfigurationQueryString**](netconfigurationquerystring.md)
* [**NetConfigurationQueryUlong**](netconfigurationqueryulong.md)
