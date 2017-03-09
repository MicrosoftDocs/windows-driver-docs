---
title: Accessing Configuration Information
---

# Accessing Configuration Information

The NetAdapterCx class extension supports a set of functions that provide access to client driver registry parameters.

Typically, the client driver reads configuration info from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function.

Start by calling [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) to get a handle to a configuration object.  You can then query it:

```cpp
NETCONFIGURATION config = NULL;

status = NetAdapterOpenConfiguration(NetAdapter, WDF_NO_OBJECT_ATTRIBUTES, &config);
if (!NT_SUCCESS(status)) {
    return status;
}

status = NetConfigurationQueryUlong(config, 0, &SomeValue, &myvalue);

NetConfigurationClose(configuration);
```
There are `NetConfiguration*` functions for querying ULONG data, strings, multi-strings (similar to REG_MULTI_SZ), binary blobs, and MAC addresses:

* [NetConfigurationAssignBinary method](netconfigurationassignbinary.md)
* [NetConfigurationAssignMultiString method](netconfigurationassignmultistring.md)
* [NetConfigurationAssignUlong method](netconfigurationassignulong.md)
* [NetConfigurationAssignUnicodeString method](netconfigurationassignunicodestring.md)
* [NetConfigurationClose method](netconfigurationclose.md)
* [NetConfigurationOpenSubConfiguration method](netconfigurationopensubconfiguration.md)
* [NetConfigurationQueryBinary method](netconfigurationquerybinary.md)
* [NetConfigurationQueryMultiString method](netconfigurationquerymultistring.md)
* [NetConfigurationQueryNetworkAddress method](netconfigurationquerynetworkaddress.md)
* [NetConfigurationQueryString method](netconfigurationquerystring.md)
* [NetConfigurationQueryUlong method](netconfigurationqueryulong.md)

