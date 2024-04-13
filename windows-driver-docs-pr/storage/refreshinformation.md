---
title: RefreshInformation Function
description: The RefreshInformation WMI method updates all tables for the HBA that corresponds to the calling instance object.
keywords: ["RefreshInformation function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- RefreshInformation
api_type:
- NA
ms.date: 10/17/2018
---

# RefreshInformation function


The **RefreshInformation** WMI method updates all tables for the HBA that corresponds to the calling instance object.

## Syntax

```ManagedCPlusPlus
void RefreshInformation(void);
```

## Parameters

This function has no parameters.

## Return value

Not applicable.

## Remarks

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

 

 






