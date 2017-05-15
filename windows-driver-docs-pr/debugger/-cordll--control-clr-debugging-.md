---
title: .cordll (Control CLR Debugging)
description: The .cordll command controls managed code debugging and the Microsoft .NET common language runtime (CLR).
ms.assetid: d46965b3-4f20-4e25-82e6-79e7fb9b4838
keywords: ["Control CLR Debugging (.cordll) command", "CLR (common language runtime)", ".cordll (Control CLR Debugging) Windows Debugging"]
topic_type:
- apiref
api_name:
- .cordll (Control CLR Debugging)
api_type:
- NA
---

# .cordll (Control CLR Debugging)


The **.cordll** command controls managed code debugging and the Microsoft .NET common language runtime (CLR).

``` syntax
.cordll [Options]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
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

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

To debug a managed application, the debugger must load a data access component (DAC) that corresponds to the CLR that the application has loaded. However, in some cases, the application loads more than one CLR. In that case, you can use the **I** parameter to specify which DAC the debugger should load. Version 2 of the CLR is named Mscorwks.dll, and version 4 of the CLR is named Clr.dll. The following example shows how to specify that the debugger should load the DAC for version 2 (mscorwks).

```
.cordll -I mscorwks -lp c:\dacFolder
```

If you omit the **I** parameter, the debugger uses version 4 by default. For example, the following two commands are equivalent.

```
.cordll -lp c:\dacFolder
.cordll -I clr -lp c:\dacFolder
```

Sos.dll is a component that is used for debugging managed code. The current version of Debugging Tools for Windows does not include any version of sos.dll. For information about how to get sos.dll, see [Getting the SOS Debugging Extension (sos.dll)](debugging-managed-code.md#getting-the-sos-debugging-extension).

The **.cordll** command is supported in kernel-mode debugging. However, this command might not work unless the necessary memory is paged in.

## <span id="see_also"></span>See also


[Debugging Managed Code Using the Windows Debugger](debugging-managed-code.md)

[SOS Debugging Extension](http://go.microsoft.com/fwlink/p/?linkid=223345)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.cordll%20%28Control%20CLR%20Debugging%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





