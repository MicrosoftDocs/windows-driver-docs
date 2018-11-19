---
title: How do I use WPP in static libraries
description: How do I use WPP in static libraries
ms.assetid: 02e13837-f8c7-4824-a4db-5e8b49fdcb59
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I use WPP in static libraries?


WPP tracing can be used within a static library in such a way that provides separate control over the tracing between the static library (.lib) and binary (.exe, .dll or .sys) that uses it.

Both the binary and library have their own control GUID. This allows tracing to be enabled in the static library, the binary, or both.

The .lib file can be accessed by using WPP at several points, as shown in the following code example. Be aware that it is not important to define the actual value of the control GUID, because the static library is not calling the WPP\_INIT\_TRACING macro, which does the actual registration with ETW.

```
#define WPP_CONTROL_GUIDS \
WPP_DEFINE_CONTROL_GUID(mylib,(0,0,0,0,0), \
WPP_DEFINE_BIT(Error) \
WPP_DEFINE_BIT(Unusual) \
WPP_DEFINE_BIT(Noise) \
)
```

The .dll, .exe, and .sys files that use the library must call WPP\_INIT\_TRACING, which will register the provider with WPP. The binary that calls the macro WPP\_INIT\_TRACING must have a copy of the WPP control GUIDs obtained by the WPP\_CONTROL\_GUID macro. Copies of the flag values are needed only if the flags defined in the static library are planned to be also used in the binary.

In the following code sample, the static library's control GUID is declared first and control GUID's flags match the flags that are defined in the library:

```
#define WPP_CONTROL_GUIDS \
WPP_DEFINE_CONTROL_GUID(SharedStaticLibs,(81b20feb,73a8,4b62,95bc,354477c97a6f), \
WPP_DEFINE_BIT(Error) \
WPP_DEFINE_BIT(Unusual) \
WPP_DEFINE_BIT(Noise) \
) \
WPP_DEFINE_CONTROL_GUID(AppSpecificFlags,(81b20fec,73a8,4b62,95bc,354477c97a6f), \
WPP_DEFINE_BIT(EntryExit) \
WPP_DEFINE_BIT(Initialization) \
WPP_DEFINE_BIT(MemoryAllocations) \
) 
```

You can select the degree of control that you need for tracing on both your component and the static library, by specifying either a separate control GUID for the .lib and the .exe files, each with its own flags, or one control GUID for both. In the sample, the .exe file is using the same flags as the .lib file.

 

 





