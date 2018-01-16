---
title: wdfkd.wdflogsave
description: The wdfkd.wdflogsave extension saves the Kernel-Mode Driver Framework (KMDF) error log records for a specified driver to an event trace log (.etl) file that you can view by using TraceView.
ms.assetid: e072d522-a418-4afb-8434-c6355d026770
keywords: ["wdfkd.wdflogsave Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdflogsave
api_type:
- NA
---

# !wdfkd.wdflogsave


The **!wdfkd.wdflogsave** extension saves the Kernel-Mode Driver Framework (KMDF) error log records for a specified driver to an event trace log (.etl) file that you can view by using TraceView.

```
!wdfkd.wdflogsave [DriverName [FileName]]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
Optional. The name of a driver. *DriverName* must not include the .sys file name extension.

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Optional. The name of the file to which the KMDF error log records should be saved. *FileName* should not include the .etl file name extension. If you omit *FileName*, the KMDF error log records are saved to the DriverName.etl file.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

If you omit the *DriverName* parameter, the default driver name is used. Use the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension to display the default driver name, and use the [**!wdfkd.wdfsetdriver**](-wdfkd-wdfsetdriver.md) extension to set the default driver name.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdflogsave%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




