---
title: Wireless displays (Miracast)
description: Wireless (Miracast) displays can optionally be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.
ms.assetid: 1645E14A-EC4A-4EB8-9AFA-6DF0466D2B1A
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wireless displays (Miracast)


Wireless (Miracast) displays can optionally be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.

For more information on the requirements of drivers and hardware to support Miracast displays, refer to the [Building best-in-class Miracast solutions with Windows 10](http://download.microsoft.com/download/3/F/9/3F9F0453-04AE-4E4B-87EF-729FF931C1F9/Building best-in-class Miracast solutions with Windows 10.docx) guide and the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**.

## <span id="Miracast_design_guide"></span><span id="miracast_design_guide"></span><span id="MIRACAST_DESIGN_GUIDE"></span>Miracast design guide


These design guide sections describe how display miniport drivers and Miracast user-mode drivers support Miracast displays:

-   [WDDM display miniport driver tasks to support Miracast wireless displays](wddm-display-miniport-driver-tasks-to-support-miracast-wireless-displays.md)
-   [Miracast user-mode driver tasks to support Miracast wireless displays](miracast-user-mode-driver-tasks-to-support-miracast-wireless-displays.md)
-   [Reporting Miracast encode chunks and statistics](reporting-miracast-encode-chunks-and-statistics.md)
-   [Calling DisplayConfig functions for a Miracast target](calling-displayconfig-functions-for-a-miracast-target.md)

## <span id="Miracast_reference"></span><span id="miracast_reference"></span><span id="MIRACAST_REFERENCE"></span>Miracast reference


These reference sections describe how to implement this capability in your drivers:

### <span id="User-mode_device_driver_interfaces__DDIs_"></span><span id="user-mode_device_driver_interfaces__ddis_"></span><span id="USER-MODE_DEVICE_DRIVER_INTERFACES__DDIS_"></span>User-mode device driver interfaces (DDIs)

<span id="Wireless_display_callback_functions_called_by_Miracast_user-mode_drivers"></span><span id="wireless_display_callback_functions_called_by_miracast_user-mode_drivers"></span><span id="WIRELESS_DISPLAY_CALLBACK_FUNCTIONS_CALLED_BY_MIRACAST_USER-MODE_DRIVERS"></span>[Wireless display callback functions called by Miracast user-mode drivers](https://msdn.microsoft.com/library/windows/hardware/dn265514)  
All functions implemented by the operating system that can be called by Miracast user-mode drivers.

<span id="Wireless_display_functions_implemented_by_Miracast_user-mode_drivers"></span><span id="wireless_display_functions_implemented_by_miracast_user-mode_drivers"></span><span id="WIRELESS_DISPLAY_FUNCTIONS_IMPLEMENTED_BY_MIRACAST_USER-MODE_DRIVERS"></span>[Wireless display functions implemented by Miracast user-mode drivers](https://msdn.microsoft.com/library/windows/hardware/dn265515)  
All functions that Miracast user-mode drivers must implement in order to enable Miracast displays.

<span id="Wireless_display__Miracast__structures_and_enumerations"></span><span id="wireless_display__miracast__structures_and_enumerations"></span><span id="WIRELESS_DISPLAY__MIRACAST__STRUCTURES_AND_ENUMERATIONS"></span>[Wireless display (Miracast) structures and enumerations](https://msdn.microsoft.com/library/windows/hardware/dn265516)  
All user-mode structures and enumerations that are used with Miracast display device driver interfaces (DDIs).

These additional user-mode structures and enumerations support Miracast displays and are new or updated for Windows 8.1:

-   [**DISPLAYCONFIG\_TARGET\_BASE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn362043) (new)
-   [**DISPLAYCONFIG\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554007) (**AdditionalSignalInfo** child structure added)
-   [**DISPLAYCONFIG\_DEVICE\_INFO\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff553924) (**DISPLAYCONFIG\_DEVICE\_INFO\_GET\_TARGET\_BASE\_TYPE** constant added)
-   [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff546625) (**AdditionalSignalInfo** child structure added)
-   [**DISPLAYCONFIG\_DEVICE\_INFO\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff553924) (**DISPLAYCONFIG\_DEVICE\_INFO\_GET\_TARGET\_BASE\_TYPE** constant added)

### <span id="Kernel-mode_DDIs"></span><span id="kernel-mode_ddis"></span><span id="KERNEL-MODE_DDIS"></span>Kernel-mode DDIs

<span id="Wireless_display__Miracast__display_callback_interface"></span><span id="wireless_display__miracast__display_callback_interface"></span><span id="WIRELESS_DISPLAY__MIRACAST__DISPLAY_CALLBACK_INTERFACE"></span>[Wireless display (Miracast) display callback interface](https://msdn.microsoft.com/library/windows/hardware/dn344650)  
All functions that are implemented by the Microsoft DirectX graphics kernel subsystem to support Miracast displays.

<span id="Wireless_display__Miracast__interface"></span><span id="wireless_display__miracast__interface"></span><span id="WIRELESS_DISPLAY__MIRACAST__INTERFACE"></span>[Wireless display (Miracast) interface](https://msdn.microsoft.com/library/windows/hardware/dn344651)  
All functions that are implemented by display miniport drivers that support Miracast displays.

These additional kernel-mode structures and enumerations support Miracast displays and are new or updated for Windows 8.1:

-   [**DXGK\_MIRACAST\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/dn322054) (new)
-   [**D3DKMDT\_VIDEO\_OUTPUT\_TECHNOLOGY**](https://msdn.microsoft.com/library/windows/hardware/ff546605) (**D3DKMDT\_VOT\_MIRACAST** constant added)
-   [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff546625) (**AdditionalSignalInfo** child structure added)
-   [**DXGK\_CHILD\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff561010) (**Miracast** child structure added)
-   [**DXGK\_CHILD\_STATUS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561015) (**StatusMiracast** constant added)
-   [**DXGKARGCB\_NOTIFY\_INTERRUPT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff557538) (**MiracastEncodeChunkCompleted** child structure added)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Wireless%20displays%20%28Miracast%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




