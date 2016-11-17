---
title: Getting started guide - Microsoft Standard Driver for 3D Printers
author: windows-driver-content
description: The Microsoft Standard Driver for 3D Printers allows developers to easily make their printer compatible with Windows 10.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: DAFC5B26-09BA-483C-B964-1DA96E77765F
---

# Getting started guide - Microsoft Standard Driver for 3D Printers


The Microsoft Standard Driver for 3D Printers allows developers to easily make their printer compatible with Windows 10. Any printer that uses Microsoft OS descriptors can be recognized as a compatible 3D printer. Using a concrete example, this article will show how to create a firmware that allows a device to be recognized as a 3D printer by Windows 10 and communicate its print capabilities.

## Introduction


The Microsoft Standard Driver relieves the burden of writing their own driver from independent hardware vendors (IHVs) who want their 3D printers to be compatible with Windows 10. Versions of Windows that are aware of Microsoft OS descriptors use control requests to retrieve the information and use it to install and configure the device without requiring any user interaction.

The general process to get a 3D printer working on Windows 10 includes the following steps:

1.  **Compatible ID**. The independent hardware vendor (IHV) has to include the "3D Print" compatible ID in the firmware of the printer. This allows the device to be recognized as a 3D printer.

2.  **Standard Driver**. Once the device is plugged in, Windows Update will download the 3D print standard driver and detect the current device as a 3D printer that uses a default configuration.

3.  **Extended properties descriptor**. Several base configurations for 3D printers are made available as part of the standard driver. A developer can therefore choose a base configuration that matches their 3D printer. On top of choosing a base configuration, a developer can override some of the properties to better match their 3D printer and include them in the new firmware.

4.  **Plug and play**. Once the firmware is burned in the flash memory of the 3D printer, whenever a user plugs it into a Windows 10 machine, the standard driver will automatically be downloaded and will use the custom print capabilities that the developer has chosen.

In the following sections, we will illustrate each of these steps using a concrete example.

For more information, see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?LinkId=533944).

## Compatible ID


To specify to the Windows operating system that we are currently using a 3D printer, we have to use the right compatible ID. The list of Microsoft Compatible ID are available at [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?LinkId=533944).

The compatible ID for a 3D printer is shown in the following table:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Compatible ID</th>
<th>Sub-compatible ID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>&quot;3DPRINT&quot;</p>
<p>(0x33 0x44 0x50 0x52 0x49 0x4E 0x54 0x00)</p></td>
<td><p>Varies</p></td>
<td><p>MS3DPRINT G-Code Printer</p></td>
</tr>
</tbody>
</table>

 

In the header file that is included in the 3D printer firmware, the IHV must specify the Compatible ID as shown here:

```
#define MS3DPRINT_CONFIG_SIZE 232

#define MS3DPRINT_OSP_SIZE (4+4+2+0x20+4+MS3DPRINT_CONFIG_SIZE)

#define MS3DPRINT_XPROP_SIZE (4+2+2+2+MS3DPRINT_OSP_SIZE)

#define SIZE_TO_DW(__size)                \
        ((uint32_t)__size) & 0xFF,        \
        (((uint32_t)__size)>>8) & 0xFF,   \
        (((uint32_t)__size)>>16) & 0xFF,  \
        (((uint32_t)__size)>>24) & 0xFF 

// CompatibleID and SubCompatibleID
static const uint8_t PROGMEM ms3dprint_descriptor[40] = {
    0x28, 0x00, 0x00, 0x00,                          // dwLength
    0x00, 0x01,                                      // bcdVersion
    0x04, 0x00,                                      // wIndex
    0x01,                                            // bCount
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,        // RESERVED
    0x00,                                            // bFirstInterfaceNumber
    0x01,                                            // RESERVED
    &#39;3&#39;, &#39;D&#39;, &#39;P&#39;, &#39;R&#39;, &#39;I&#39;, &#39;N&#39;, &#39;T&#39;, 0x00,         // compatibleID ("3DPRINT")
                                                 // subCompatibleID
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00   /*        */  
,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00               // RESERVED
};
```

This line in the code above is the compatible ID of a 3D Printer:

```
&#39;3&#39;, &#39;D&#39;, &#39;P&#39;, &#39;R&#39;, &#39;I&#39;, &#39;N&#39;, &#39;T&#39;, 0x00,         // compatibleID ("3DPRINT")
```

With this specific configuration, IHVs can compile their firmware and flash the device. Then when the device is plugged in, the 3D Print Standard Driver will automatically get downloaded from Windows Update.

At this stage the printer is using the standard driver default configuration, the parameters used by the default configuration are accessible in the folder %SYSTEMROOT%\\System32\\MS3DPrint in the file StandardGCode.xml. Additionally, a developer can chose to use a different base configuration, a list of base configurations are available in the same folder %SYSTEMROOT%\\System32\\MS3DPrint. This list is regularly populated with new configuration as new 3D printers emerge on the market.

## Extended Properties OS Feature Descriptor


As stated in the above section, IHVs have access to several base configurations. This has the advantage of minimizing the amount of information that has to be stored in the printer’s flash memory. Developers can inspect the base configurations made available and choose the one that is the closest to their printers. In this example we are going to choose the SD card base configuration and override some of the properties with the parameters below:

| Parameters            | Value  |
|-----------------------|--------|
| Job3DOutputAreaWidth  | 250000 |
| Job3DOutputAreaDepth  | 260000 |
| Job3DOutputAreaHeight | 270000 |
| Filamentdiameter      | 2850   |

 

For more information about these parameters, please refer to the *MS3DPrint Standard G-Code Driver.docx* document in the [3D Printing SDK](http://go.microsoft.com/fwlink/p/?LinkId=394375) documentation.

To specify which base configuration to use and which parameters to override, the developer has to specify it through the Extended Properties OS Feature Descriptor as shown here:

```
// Modifiers to the base configuration
static const uint8_t PROGMEM ms3dprint_properties_descriptor[] = {
    SIZE_TO_DW(MS3DPRINT_XPROP_SIZE),                   // dwLength
    0x00, 0x01,                                         // bcdVersion
    0x05, 0x00,                                         // wIndex
    0x01, 0x00,                                         // wCount
    
    SIZE_TO_DW(MS3DPRINT_OSP_SIZE),                     // dwSize
    0x07, 0x00, 0x00, 0x00,                             // dwPropertyDataType  (1=REG_SZ, 4=REG_DWORD, 7=REG_MULTI_SZ)

    0x20, 0x00,                                         // wPropertyNameLength
    &#39;M&#39;, 0x0, &#39;S&#39;, 0x0, &#39;3&#39;, 0x0, &#39;D&#39;, 0x0,             // bPropertyName
    &#39;P&#39;, 0x0, &#39;r&#39;, 0x0, &#39;i&#39;, 0x0, &#39;n&#39;, 0x0,
    &#39;t&#39;, 0x0, &#39;C&#39;, 0x0, &#39;o&#39;, 0x0, &#39;n&#39;, 0x0,
    &#39;f&#39;, 0x0, &#39;i&#39;, 0x0, &#39;g&#39;, 0x0, 0x0, 0x0,

    SIZE_TO_DW(MS3DPRINT_CONFIG_SIZE),                  // dwPropertyDataLength

    // Data
    0x42, 0x00, 0x61, 0x00, 0x73, 0x00, 0x65, 0x00, 0x3D, 0x00, 0x53, 0x00, 0x44, 0x00, 0x00, 0x00,  /* Base=SD  */  
    0x4A, 0x00, 0x6F, 0x00, 0x62, 0x00, 0x33, 0x00, 0x44, 0x00, 0x4F, 0x00, 0x75, 0x00, 0x74, 0x00,  /* Job3DOut */  
    0x70, 0x00, 0x75, 0x00, 0x74, 0x00, 0x41, 0x00, 0x72, 0x00, 0x65, 0x00, 0x61, 0x00, 0x57, 0x00,  /* putAreaW */  
    0x69, 0x00, 0x64, 0x00, 0x74, 0x00, 0x68, 0x00, 0x3D, 0x00, 0x32, 0x00, 0x35, 0x00, 0x30, 0x00,  /* idth=250 */  
    0x30, 0x00, 0x30, 0x00, 0x30, 0x00, 0x00, 0x00, 0x4A, 0x00, 0x6F, 0x00, 0x62, 0x00, 0x33, 0x00,  /* 000 Job3 */  
    0x44, 0x00, 0x4F, 0x00, 0x75, 0x00, 0x74, 0x00, 0x70, 0x00, 0x75, 0x00, 0x74, 0x00, 0x41, 0x00,  /* DOutputA */  
    0x72, 0x00, 0x65, 0x00, 0x61, 0x00, 0x44, 0x00, 0x65, 0x00, 0x70, 0x00, 0x74, 0x00, 0x68, 0x00,  /* reaDepth */  
    0x3D, 0x00, 0x32, 0x00, 0x36, 0x00, 0x30, 0x00, 0x30, 0x00, 0x30, 0x00, 0x30, 0x00, 0x00, 0x00,  /* =260000  */  
    0x4A, 0x00, 0x6F, 0x00, 0x62, 0x00, 0x33, 0x00, 0x44, 0x00, 0x4F, 0x00, 0x75, 0x00, 0x74, 0x00,  /* Job3DOut */  
    0x70, 0x00, 0x75, 0x00, 0x74, 0x00, 0x41, 0x00, 0x72, 0x00, 0x65, 0x00, 0x61, 0x00, 0x48, 0x00,  /* putAreaH */  
    0x65, 0x00, 0x69, 0x00, 0x67, 0x00, 0x68, 0x00, 0x74, 0x00, 0x3D, 0x00, 0x32, 0x00, 0x37, 0x00,  /* eight=27 */  
    0x30, 0x00, 0x30, 0x00, 0x30, 0x00, 0x30, 0x00, 0x00, 0x00, 0x66, 0x00, 0x69, 0x00, 0x6C, 0x00,  /* 0000 fil */  
    0x61, 0x00, 0x6D, 0x00, 0x65, 0x00, 0x6E, 0x00, 0x74, 0x00, 0x64, 0x00, 0x69, 0x00, 0x61, 0x00,  /* amentdia */  
    0x6D, 0x00, 0x65, 0x00, 0x74, 0x00, 0x65, 0x00, 0x72, 0x00, 0x3D, 0x00, 0x32, 0x00, 0x38, 0x00,  /* meter=28 */  
    0x35, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00                                                   /* 50       */  
};
```

Information regarding the extended properties OS feature descriptor are in the *OS\_Desc\_Ext\_Prop.doc* file available on MSDN at [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?LinkId=533944).

## Verifying the print capabilities


Once the device has the firmware burned in flash memory , the device will automatically be detected by Windows 10 and the print capabilities will be stored in registry.

![installing compatable 3d printer ](images/installing-compatible-3d-printer.png)

It is very important that the IHV changes the VID/PID of the device to their own. You should never use the Vendor ID (VID) or Product ID (PID) of another existing device as the operating system will not be able to detect the device properly as the VID and PID take priority over the OS descriptor.

If the device has been properly installed, the device should be listed in **Devices and Printers**.

![devices and printers](images/devices-and-printers-3d.png)

In the **Device Manager**, the matching device id and the compatible id can be verified.

![device manager](images/device-manager-3d.png)

![device manager details tab - matching device id](images/device-manager-details-3d.png)

![device manager details tab - compatible ids](images/device-manager-details2-3d.png)

The USB driver properties can be obtained by visiting the registry at **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USB**.

![edit multi-string value in usb registry](images/usb-registry-3d.png)

The 3D Print driver properties can be obtained by visiting the registry at **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print\\Printers**.

![view 3d print driver properties in the registry](images/printers-registry-3d.png)

## Additional resources


For more information, see the following documents and resources:

[3D Printing in Windows](http://go.microsoft.com/fwlink/p/?LinkId=534206)

[3D Printing SDK (MSI download)](http://go.microsoft.com/fwlink/p/?LinkId=394375)

[Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?LinkId=533944)

[USB 2.0 Specification](http://go.microsoft.com/fwlink/p/?linkid=533945)

You can also contact the Microsoft 3D Printing team at [Ask 3D Printing Questions](http://go.microsoft.com/fwlink/p/?LinkId=534751) (ask3dprint@microsoft.com).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Getting%20started%20guide%20-%20Microsoft%20Standard%20Driver%20for%203D%20Printers%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


