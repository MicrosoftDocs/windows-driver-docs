---
title: DevCon Dp\_delete
description: Deletes a third-party (OEM) driver package from the driver store on the local computer. This command deletes the INF file, the PNF file, and the associated catalog file (.cat).
ms.assetid: bc9d8d66-4aa1-423b-b907-40a8c0194eb1
keywords: ["DevCon Dp_delete Driver Development Tools"]
topic_type:
- apiref
api_name:
- DevCon Dp_delete
api_type:
- NA
---

# DevCon Dp\_delete


Deletes a third-party (OEM) driver package from the driver store on the local computer. This command deletes the INF file, the PNF file, and the associated catalog file (.cat).

``` syntax
    devcon dp_delete [-f] inf

   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-f______"></span><span id="_______-F______"></span> **-f**   
This parameter deletes the driver package even if a device is using it at the time.

<span id="_______inf______"></span><span id="_______INF______"></span> *inf*   
The OEM\*.inf file name of the INF file. Windows assigns a file name with this format to the INF file when you add the driver package to the driver store, such as by using [**DevCon dp\_add**](devcon-dp-add.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon dp_delete oem2.inf
devcon dp_delete oem0.inf -f
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20DevCon%20Dp_delete%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




