---
title: Using GetOptions and SetOptions
author: windows-driver-content
description: Using GetOptions and SetOptions
MS-HAID:
- 'pscript\_9c9f919f-341e-45bb-ab32-a8e215cecb41.xml'
- 'print.using\_getoptions\_and\_setoptions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c8b5c235-0b74-47c8-b6ba-eba810a8467b
keywords: ["GetOptions", "SetOptions"]
---

# Using GetOptions and SetOptions


## <a href="" id="ddk-using-getoptions-and-setoptions-gg"></a>


**GetOptions** can be called to retrieve the driver's current setting for features whose keywords are listed in the buffer pointed to by the *pmszFeaturesRequested* input parameter.

For example, in a call to **GetOptions**, suppose that the *pmszFeaturesRequested* input buffer contains this string (in MULTI\_SZ format):

```
"PageSize\0Duplex\0Resolution\0\0"
```

After the **GetOptions** method returns, the output *pmszFeatureOptionBuf* could contain the following string (also in MULTI\_SZ format):

```
"PageSize\0Letter\0Duplex\0DuplexTumble\0Resolution\0300dpi\0\0"
```

This example shows that **GetOptions** retrieved the option keywords for PageSize (Letter), Duplex (DuplexTumble), and Resolution (300dpi).

**SetOptions** can be called to change the driver's current setting based on the feature/option keyword pairs in the *pmszFeatureOptionBuf* input buffer.

There are two categories of features that are supported:

[PPD Features](ppd-features.md)

[Driver Features](driver-features.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20GetOptions%20and%20SetOptions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


