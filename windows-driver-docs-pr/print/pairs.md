---
title: Pairs
author: windows-driver-content
description: Pairs
ms.assetid: 156e6b10-74c2-4702-b0be-b9d209c02070
keywords: ["GPD file entries WDK Unidrv , pairs", "pairs WDK GPD files"]
---

# Pairs


## <a href="" id="ddk-pairs-gg"></a>


To assign a pair of values to an attribute, use the PAIR keyword. The format is:

**PAIR** ( *Value1* , *Value2* )

where *Value1* and *Value2* are [numeric values](numeric-values.md). For example, the cursor origin position can be specified in [master units](master-units.md) as follows:

```
*CursorOrigin: PAIR(120, 100)
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pairs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


