---
title: Loading an OpenGL Installable Client Driver
description: Loading an OpenGL Installable Client Driver
ms.assetid: 2b244bbf-f26c-4307-a347-a29e12c6d496
keywords:
- OpenGL ICD WDK display
- loading drivers WDK display
- ICD WDK display
- installable client driver WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Loading an OpenGL Installable Client Driver


The OpenGL runtime accesses the registry to determine which OpenGL installable client driver (ICD) to load. To load the OpenGL ICD, the OpenGL runtime:

-   Determines the name, version, and flags that are associated with the OpenGL ICD by calling the [**D3DKMTQueryAdapterInfo**](https://msdn.microsoft.com/library/windows/hardware/ff547100) function with the KMTQAITYPE\_UMOPENGLINFO value set in the **Type** member of the [**D3DKMT\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff548203) structure that the *pData* parameter points to.

-   Checks the version number of the OpenGL ICD that **D3DKMTQueryAdapterInfo** returns to validate the version of the OpenGL ICD.

-   Loads the OpenGL ICD by using the name of the OpenGL ICD.

-   Initializes access to the OpenGL ICD's functions.
    **Note**   To obtain a license for the OpenGL ICD Development Kit, contact the [OpenGL Issues](mailto:opengl@microsoft.com) team.

     

To locate the name of the OpenGL ICD, [**D3DKMTQueryAdapterInfo**](https://msdn.microsoft.com/library/windows/hardware/ff547100) searches the registry in the following key:

```registry
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

 

 





