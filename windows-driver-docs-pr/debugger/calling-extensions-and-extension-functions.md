---
title: Calling Extensions and Extension Functions
description: Calling Extensions and Extension Functions
ms.assetid: 0582cdc2-7059-42db-878b-28767a6fe850
keywords: ["Debugger Engine API, calling extensions"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Calling Extensions and Extension Functions


To load an extension library (or to obtain a handle for an already loaded extension library), use [**AddExtension**](https://msdn.microsoft.com/library/windows/hardware/ff537892). An extension library can be unloaded with [**RemoveExtension**](https://msdn.microsoft.com/library/windows/hardware/ff554497).

Extension commands can be called using [**CallExtension**](https://msdn.microsoft.com/library/windows/hardware/ff539023).

### <span id="extension_functions"></span><span id="EXTENSION_FUNCTIONS"></span>Extension Functions

*Extension functions* are functions that are exported by extension libraries. They can use any function prototype and are called directly using C function pointers.

They are not extension commands and are not available via debugger commands. Extension functions cannot be called remotely; they must be called directly. Hence they cannot be used from debugging clients. They can only be called when the client object is inside the host engine - when not remotely debugging or when using a smart client.

Extension functions are identified within extension libraries by the "\_EFN\_" prepended to their names.

To obtain a pointer to an extension function, use [**GetExtensionFunction**](https://msdn.microsoft.com/library/windows/hardware/ff546733). The type of this function pointer should match the prototype of the extension function. The extension function can now be called just like any other function pointer in C.

### <span id="example"></span><span id="EXAMPLE"></span>Example

If the following extension function was included in an extension library and loaded into the debugger engine:

```cpp
HRESULT CALLBACK
_EFN_GetObject(IDebugClient * client, SomeObject * obj);
```

It could be called using:

```cpp
typedef ULONG (CALLBACK * GET_OBJECT)(IDebugClient * client, SomeObject * obj);



HRESULT status = S_OK;
GET_OBJECT extFn = NULL;
SomeObject myObj;

if (g_DebugControl->
        GetExtensionFunction(0,
                             "GetObject",
                             (FARPROC *) &extFn ) == S_OK &&
    extFn)
{
    status = (*extFn)(client, &myObj);
}
```

 

 





