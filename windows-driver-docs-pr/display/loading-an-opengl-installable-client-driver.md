---
title: Loading an OpenGL Installable Client Driver
description: Loading an OpenGL Installable Client Driver
keywords:
- OpenGL ICD WDK display
- loading drivers WDK display
- ICD WDK display
- installable client driver WDK display
ms.date: 11/17/2021
ms.localizationpriority: medium
---

# Loading an OpenGL Installable Client Driver

The OpenGL runtime accesses the registry to determine which OpenGL installable client driver (ICD) to load. To load the OpenGL ICD, the OpenGL runtime:

- Determines the name, version, and flags that are associated with the OpenGL ICD by calling the [**D3DKMTQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtqueryadapterinfo) function with the KMTQAITYPE_UMOPENGLINFO value set in the **Type** member of the [**D3DKMT_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_queryadapterinfo) structure that the *pData* parameter points to.

- Checks the version number of the OpenGL ICD that **D3DKMTQueryAdapterInfo** returns to validate the version of the OpenGL ICD.

- Loads the OpenGL ICD by using the name of the OpenGL ICD.

- Initializes access to the OpenGL ICD's functions.

To locate the name of the OpenGL ICD, [**D3DKMTQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtqueryadapterinfo) searches the registry in the following key:

```registry
HKLM/System/CurrentControlSet/Control/Class/{Adapter GUID}/0000/
```

This key also contains the names of the [Microsoft Direct3D user-mode display drivers](initializing-communication-with-the-direct3d-user-mode-display-driver.md). This key contains four registry entries for 32-bit Windows Vista display drivers that are used on 32-bit Windows Vista and four entries for 32-bit Windows Vista display drivers that are used on 64-bit Windows Vista. The following entries are for 32-bit Windows Vista display drivers that are used on 32-bit Windows Vista:

| Entry | Type | Explanation |
| ----- | ---- | ----------- |
| **UserModeDriverName** | REG_SZ    | The name of the Direct3D user-mode display driver, which is required for the operation of a Direct3D rendering device regardless of whether the operating system supports an OpenGL ICD. |
| **OpenGLDriverName**   | REG_SZ    | The name of the OpenGL ICD. For example, if the OpenGL ICD is *Mydriver.dll*, the value of this entry is **Mydriver.dll**. |
| **OpenGLVersion**      | REG_DWORD | The version number of the OpenGL ICD that the OpenGL runtime uses to validate the version of the OpenGL ICD.
| **OpenGLFlags**        | REG_DWORD | A flag bitmask. Currently, bit 0 (0x00000001) is set for compatibility. When bit 1 (0x00000002) is set, the OpenGL runtime does not call the ICD's finish function before the runtime calls the ICD's swap-buffers function. |

The following entries are for 32-bit Windows Vista display drivers that are used on 64-bit Windows Vista:

| Entry | Type | Explanation |
| ----- | ---- | ----------- |
| **UserModeDriverNameWow** | REG_SZ    | The name of the 32-bit Microsoft Direct3D user-mode display driver for 64-bit Windows Vista. |
| **OpenGLDriverNameWow**   | REG_SZ    | The name of the 32-bit OpenGL ICD for 64-bit Windows Vista. |
| **OpenGLVersionWow**      | REG_DWORD | The version number of the 32-bit OpenGL ICD for 64-bit Windows Vista. |
| **OpenGLFlagsWow**        | REG_DWORD | A flag bitmask of the 32-bit OpenGL ICD for 64-bit Windows Vista. |
