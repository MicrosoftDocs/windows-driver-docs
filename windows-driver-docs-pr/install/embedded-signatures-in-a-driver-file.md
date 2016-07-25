---
title: Embedded Signatures in a Driver File
description: Embedded Signatures in a Driver File
ms.assetid: 21941c7b-4f9a-424c-9984-3048a53398b6
keywords: ["embedded signatures WDK driver signing", "driver signing WDK , embedded", "signing drivers WDK , embedded", "digital signatures WDK , embedded", "signatures WDK , embedded"]
---

# Embedded Signatures in a Driver File


In 64-bit versions of Windows Vista and later versions of Windows, the [kernel-mode code signing requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) state that a released kernel-mode [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) must have an embedded [Software Publisher Certificate (SPC)](software-publisher-certificate.md) signature. An embedded signature is not required for drivers that are not boot-start drivers.

**Note**  Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard and the Windows Hardware Dev Center Dashboard requires an EV certificate. For more info about these changes, see [Driver Signing Changes in Windows 10](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/04/01/driver-signing-changes-in-windows-10.aspx).

 

Having an embedded signature saves significant time during system startup because there is no need for the system loader to locate the [catalog file](catalog-files.md) for the driver at system startup. A typical computer, which is running Windows Vista or a later version of Windows, might have many different catalog files in the catalog root store (*%System%\\CatRoot*). Locating the correct catalog file to verify the thumbprint of a driver file can require a substantial amount of time.

In addition to the load-time signature requirement that is enforced by the kernel-mode code signing policy, Plug and Play (PnP) device installation also enforces an install-time signing requirement. To comply with the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows, a [driver package](driver-packages.md) for a PnP device must have a signed catalog file.

Embedded signatures do not interfere with the signature of a catalog file because the thumbprints that are contained in a catalog file and the thumbprint in an embedded signature selectively exclude the signature part of the driver file.

Driver files are signed by using the [SignTool](installing-a-catalog-file-by-using-signtool.md) tool.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Embedded%20Signatures%20in%20a%20Driver%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




