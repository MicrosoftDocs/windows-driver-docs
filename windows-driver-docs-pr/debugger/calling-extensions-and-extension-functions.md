---
title: Calling Extensions and Extension Functions
description: Calling Extensions and Extension Functions
ms.assetid: 0582cdc2-7059-42db-878b-28767a6fe850
keywords: ["Debugger Engine API, calling extensions"]
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

```
HRESULT CALLBACK
_EFN_GetObject(IDebugClient * client, SomeObject * obj);
```

It could be called using:

```
typedef ULONG (CALLBACK * GET_OBJECT)(IDebugClient * client, SomeObject * obj);



HRESULT status = S_OK;
GET_OBJECT extFn = NULL;
SomeObject myObj;

if (g_DebugControl->
        GetExtensionFunction(0,
                             "GetObject",
                             (FARPROC *) &amp;extFn ) == S_OK &amp;&amp;
    extFn)
{
    status = (*extFn)(client, &amp;myObj);
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Calling%20Extensions%20and%20Extension%20Functions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




