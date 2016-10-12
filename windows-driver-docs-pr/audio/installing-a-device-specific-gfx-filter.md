---
title: Installing a Device-Specific GFX Filter
description: Installing a Device-Specific GFX Filter
ms.assetid: f917bb0d-eff8-4f1f-b7ad-3d135495e6e8
keywords: ["GFX filters WDK audio , installing"]
---

# Installing a Device-Specific GFX Filter


## <span id="installing_a_device_specific_gfx_filter"></span><span id="INSTALLING_A_DEVICE_SPECIFIC_GFX_FILTER"></span>


In Windows Server 2003 and Windows XP, the operating system provides a setup tool that enables automatic loading and connection of a vendor-supplied global effect that is designed for a specific audio device.

You can access the global effect through the **Multimedia** applet in Control Panel. The **Multimedia** applet can do the following:

-   Enumerate audio devices.

-   Indicate the GFX that is currently applied to each audio device.

-   Enumerate the GFX filters that are available for each audio device.

-   Select which GFX filter is applied to an audio device.

-   Invoke a vendor-supplied GFX-specific user interface for each GFX instance.

-   Remove GFX filters from an audio graph.

When the driver is installed, the installation process loads information about the proprietary GFX filter factory of the vendor into a registry path that has the following format:

&lt;*DIRegKey*&gt; \\**Gfx**\\**AutoLoad**\\ &lt;*GfxAutoLoadInst*&gt;

In this path, *DIRegKey* represents the subpath for the filter's KSCATEGORY\_AUDIO device-interface registry key, **Gfx** and **AutoLoad** are both literal subkey names, and *GfxAutoLoadInst* represents the subkey that contains the information that the operating system needs to automatically load the GFX filter factory.

The vendor supplies an INF file that installs the GFX filter factory. This file uses an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) to add the registry subkey **AutoLoad** to the device's **Gfx** key. Under the **AutoLoad** key, the INF file adds one or more *GfxAutoLoadInst* subkeys and assigns arbitrary names to these subkeys. Typically these subkeys are named "0," "1," "2," and so on. Most GFX drivers require only one subkey and assign the name "0" to that subkey. The *GfxAutoLoadInst* subkey contains the values that are shown in the following table.

Value name
Description
\[Data Type\]
**NewAutoLoad**
\[REG\_DWORD\]
Indicates whether the audio system has processed this *GfxAutoLoadInst* registry key.

1 = Audio system needs to process this registry key.
0 = Audio system has processed this registry key.
The **AddReg** directive in the GFX driver's INF file sets this value to one. The directives in the add-registry-section use the FLG\_ADDREG\_NOCLOBBER flag so that the audio system does not reprocess the registry entries if the GFX driver is only being updated.
After the audio system processes this registry information, it sets this value to zero.

**Type**
\[REG\_DWORD\]
Specifies whether the system should load the GFX filter as a render or capture GFX.

1 = render
2 = capture

**HardwareId**
\[REG\_MULTI\_SZ\]
The Plug and Play (PnP) device IDs of the hardware devices that expose the rendering or capture device interfaces through which this GFX filter is managed.

**ReferenceString**
\[REG\_SZ\]
The reference string that is used by the hardware device to call [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) when registering the rendering or capture device interface through which this GFX filter is managed.

 

The *GfxAutoLoadInst* key should also contain a subkey that is named **UserInterface\\CLSID**. This subkey contains the information that the operating system needs to identify the vendor's GFX user interface. The subkey's value is shown in the table below.

Value name
Description
\[Data Type\]

**(Default)**
\[REG\_SZ\]
String representation of the CLSID of the COM object that implements the GFX-specific user interface.

 

Given the registry information that is described in the previous tables, the operating system can find the device interfaces that it needs to load the hardware-specific GFX filter.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20a%20Device-Specific%20GFX%20Filter%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


