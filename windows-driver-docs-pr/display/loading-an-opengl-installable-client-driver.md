---
title: Loading an OpenGL Installable Client Driver
description: Loading an OpenGL Installable Client Driver
ms.assetid: 2b244bbf-f26c-4307-a347-a29e12c6d496
keywords:
- OpenGL ICD WDK display
- loading drivers WDK display
- ICD WDK display
- installable client driver WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Loading an OpenGL Installable Client Driver


The OpenGL runtime accesses the registry to determine which OpenGL installable client driver (ICD) to load. To load the OpenGL ICD, the OpenGL runtime:

-   Determines the name, version, and flags that are associated with the OpenGL ICD by calling the [**D3DKMTQueryAdapterInfo**](https://msdn.microsoft.com/library/windows/hardware/ff547100) function with the KMTQAITYPE\_UMOPENGLINFO value set in the **Type** member of the [**D3DKMT\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff548203) structure that the *pData* parameter points to.

-   Checks the version number of the OpenGL ICD that **D3DKMTQueryAdapterInfo** returns to validate the version of the OpenGL ICD.

-   Loads the OpenGL ICD by using the name of the OpenGL ICD.

-   Initializes access to the OpenGL ICD's functions.
    **Note**   To obtain a license for the OpenGL ICD Development Kit, contact the [OpenGL Issues](mailto:opengl@microsoft.com) team.

     

To locate the name of the OpenGL ICD, [**D3DKMTQueryAdapterInfo**](https://msdn.microsoft.com/library/windows/hardware/ff547100) searches the registry in the following key:

```
HKLM/System/CurrentControlSet/Control/Class/{Adapter GUID}/0000/
```

This key also contains the names of the [Microsoft Direct3D user-mode display drivers](initializing-communication-with-the-direct3d-user-mode-display-driver.md). This key contains four registry entries for 32-bit Windows Vista display drivers that are used on 32-bit Windows Vista and four entries for 32-bit Windows Vista display drivers that are used on 64-bit Windows Vista. The following entries are for 32-bit Windows Vista display drivers that are used on 32-bit Windows Vista:

<span id="UserModeDriverName"></span><span id="usermodedrivername"></span><span id="USERMODEDRIVERNAME"></span>**UserModeDriverName**  
REG\_SZ

The name of the Direct3D user-mode display driver, which is required for the operation of a Direct3D rendering device regardless of whether the operating system supports an OpenGL ICD.

<span id="OpenGLDriverName"></span><span id="opengldrivername"></span><span id="OPENGLDRIVERNAME"></span>**OpenGLDriverName**  
REG\_SZ

The name of the OpenGL ICD. For example, if the OpenGL ICD is *Mydriver.dll*, the value of this entry is **Mydriver.dll**.

<span id="OpenGLVersion"></span><span id="openglversion"></span><span id="OPENGLVERSION"></span>**OpenGLVersion**  
REG\_DWORD

The version number of the OpenGL ICD that the OpenGL runtime uses to validate the version of the OpenGL ICD.

<span id="OpenGLFlags"></span><span id="openglflags"></span><span id="OPENGLFLAGS"></span>**OpenGLFlags**  
REG\_DWORD

A flag bitmask. Currently, bit 0 (0x00000001) is set for compatibility. When bit 1 (0x00000002) is set, the OpenGL runtime does not call the ICD's finish function before the runtime calls the ICD's swap-buffers function.

The following entries are for 32-bit Windows Vista display drivers that are used on 64-bit Windows Vista:

<span id="UserModeDriverNameWow"></span><span id="usermodedrivernamewow"></span><span id="USERMODEDRIVERNAMEWOW"></span>**UserModeDriverNameWow**  
REG\_SZ

The name of the 32-bit Microsoft Direct3D user-mode display driver for 64-bit Windows Vista.

<span id="OpenGLDriverNameWow"></span><span id="opengldrivernamewow"></span><span id="OPENGLDRIVERNAMEWOW"></span>**OpenGLDriverNameWow**  
REG\_SZ

The name of the 32-bit OpenGL ICD for 64-bit Windows Vista.

<span id="OpenGLVersionWow"></span><span id="openglversionwow"></span><span id="OPENGLVERSIONWOW"></span>**OpenGLVersionWow**  
REG\_DWORD

The version number of the 32-bit OpenGL ICD for 64-bit Windows Vista.

<span id="OpenGLFlagsWow"></span><span id="openglflagswow"></span><span id="OPENGLFLAGSWOW"></span>**OpenGLFlagsWow**  
REG\_DWORD

A flag bitmask of the 32-bit OpenGL ICD for 64-bit Windows Vista.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Loading%20an%20OpenGL%20Installable%20Client%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




