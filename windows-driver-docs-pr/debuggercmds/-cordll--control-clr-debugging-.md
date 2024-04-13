---
title: ".cordll (Control CLR Debugging)"
description: "The .cordll command controls managed code debugging and the Microsoft .NET common language runtime (CLR)."
keywords: ["Control CLR Debugging (.cordll) command", "CLR (common language runtime)", ".cordll (Control CLR Debugging) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .cordll (Control CLR Debugging)
api_type:
- NA
---

# .cordll (Control CLR Debugging)

The **.cordll** command controls managed code debugging and the Microsoft .NET common language runtime (CLR).

```dbgsyntax
.cordll [Options]
```

## Parameters

*Options*
One or more of the following options:

<span id="-l___lower-case_L_"></span><span id="-l___lower-case_l_"></span><span id="-L___LOWER-CASE_L_"></span>**-l** (lower-case L)  
Loads the CLR debugging modules.

<span id="-I_Module___upper-case_i__"></span><span id="-i_module___upper-case_i__"></span><span id="-I_MODULE___UPPER-CASE_I__"></span>**-I** **** *Module* (upper-case i)   
Specifies the name or base address of the CLR module to be debugged. For more information, see Remarks.

<span id="-u"></span><span id="-U"></span>**-u**  
Unloads the CLR debugging modules.

<span id="-e"></span><span id="-E"></span>**-e**  
Enables CLR debugging.

<span id="-d"></span><span id="-D"></span>**-d**  
Disables CLR debugging.

<span id="-D"></span><span id="-d"></span>**-D**  
Disables CLR debugging and unloads the CLR debugging modules.

<span id="-N"></span><span id="-n"></span>**-N**  
Reloads the CLR debugging modules.

<span id="-lp_Path"></span><span id="-lp_path"></span><span id="-LP_PATH"></span>**-lp** **** *Path*  
Specifies the directory path of the CLR debugging modules.

<span id="-se"></span><span id="-SE"></span>**-se**  
Enables using the short name of the CLR debugging module, mscordacwks.dll.

<span id="-sd"></span><span id="-SD"></span>**-sd**  
Disables using the short name of the CLR debugging module, mscordacwks.dll. Instead, the debugger uses the long name of the CLR debugging module, mscordacwks\_&lt;spec&gt;.dll. Turning off short name usage enables you to avoid having your local CLR used if you are concerned about mismatches.

<span id="-ve"></span><span id="-VE"></span>**-ve**  
Turns on verbose mode for CLR module loading.

<span id="-vd"></span><span id="-VD"></span>**-vd**  
Turns off verbose mode for CLR module loading.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

To debug a managed application, the debugger must load a data access component (DAC) that corresponds to the CLR that the application has loaded. However, in some cases, the application loads more than one CLR. In that case, you can use the **I** parameter to specify which DAC the debugger should load. Version 2 of the CLR is named Mscorwks.dll, and version 4 of the CLR is named Clr.dll. The following example shows how to specify that the debugger should load the DAC for version 2 (mscorwks).

```dbgcmd
.cordll -I mscorwks -lp c:\dacFolder
```

If you omit the **I** parameter, the debugger uses version 4 by default. For example, the following two commands are equivalent.

```dbgcmd
.cordll -lp c:\dacFolder
.cordll -I clr -lp c:\dacFolder
```

Sos.dll is a component that is used for debugging managed code. The current version of Debugging Tools for Windows does not include any version of sos.dll. For information about how to get sos.dll, see *Getting the SOS Debugging Extension (sos.dll)* in [Debugging Managed Code Using the Windows Debugger](../debugger/debugging-managed-code.md).

The **.cordll** command is supported in kernel-mode debugging. However, this command might not work unless the necessary memory is paged in.

## See also

[Debugging Managed Code Using the Windows Debugger](../debugger/debugging-managed-code.md)

[SOS Debugging Extension](/dotnet/framework/tools/sos-dll-sos-debugging-extension)

