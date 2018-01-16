---
title: RefreshInformation function
description: The RefreshInformation WMI method updates all tables for the HBA that corresponds to the calling instance object.
ms.assetid: da78db30-0498-4d44-b5bc-76d08dc15938
keywords: ["RefreshInformation function Storage Devices"]
topic_type:
- apiref
api_name:
- RefreshInformation
api_type:
- NA
---

# RefreshInformation function


The **RefreshInformation** WMI method updates all tables for the HBA that corresponds to the calling instance object.

Syntax
------

```ManagedCPlusPlus
void RefreshInformation(void);
```

Parameters
----------

This function has no parameters.

Return value
------------

Not applicable.

Remarks
-------

The **RefreshInformation** WMI method refreshes port attribute data that is retrieved by the following WMI methods:

[**GetDiscoveredPortAttributes**](getdiscoveredportattributes.md)

[**GetFC3MgmtInfo**](getfc3mgmtinfo.md)

[**GetFC4Statistics**](getfc4statistics.md)

[**GetFCPStatistics**](getfcpstatistics.md)

[**GetPortAttributesByWWN**](getportattributesbywwn.md)

This WMI method belongs to the [MSFC\_HBAAdapterMethods WMI Class](msfc-hbaadaptermethods-wmi-class.md).

## <span id="see_also"></span>See also


[**GetDiscoveredPortAttributes**](getdiscoveredportattributes.md)

[**GetFC3MgmtInfo**](getfc3mgmtinfo.md)

[**GetFC4Statistics**](getfc4statistics.md)

[**GetFCPStatistics**](getfcpstatistics.md)

[**GetPortAttributesByWWN**](getportattributesbywwn.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20RefreshInformation%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





