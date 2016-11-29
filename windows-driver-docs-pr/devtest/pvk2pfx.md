---
title: Pvk2Pfx
description: Pvk2Pfx (Pvk2Pfx.exe) is a command-line tool copies public key and private key information contained in .spc, .cer, and .pvk files to a Personal Information Exchange (.pfx) file.
ms.assetid: f3fb3703-0e33-4d7f-b2ad-52bc035e01de
keywords: ["Pvk2Pfx Driver Development Tools"]
topic_type:
- apiref
api_name:
- Pvk2Pfx
api_type:
- NA
---

# Pvk2Pfx


Pvk2Pfx (Pvk2Pfx.exe) is a command-line tool copies public key and private key information contained in .spc, .cer, and .pvk files to a Personal Information Exchange (.pfx) file.

``` syntax
    pvk2pfx /pvk 
    pvkfilename.pvk [/pi pvkpassword] /spc spcfilename.ext [/pfx pfxfilename.pfx [/po pfxpassword] [/f]]
```

### <span id="switches_and_arguments"></span><span id="SWITCHES_AND_ARGUMENTS"></span>Switches and Arguments

<span id="_PVK_PVKFILENAME.PVK"></span>**/pvk** *pvkfilename.pvk*  
Specifies the name of a .pvk file.

<span id="_SPC_SPCFILENAME.EXT"></span>**/spc** *spcfilename.ext*  
Specifies the name and extension of the [Software Publisher Certificate (SPC)](https://msdn.microsoft.com/library/windows/hardware/ff552299) file that contains the certificate. The file can be either a .spc file or a .cer file.

<span id="_PFX_PFXFILENAME.PFX"></span>**/pfx** *pfxfilename.pfx*  
Specifies the name of a .pfx file.

<span id="_pi_pvkpassword"></span><span id="_PI_PVKPASSWORD"></span>**/pi** *pvkpassword*  
Specifies the password for the .pvk file.

<span id="_po_pfxpassword"></span><span id="_PO_PFXPASSWORD"></span>**/po** *pfxpassword*  
Specifies a password for the .pfx file. If a password for the .pfx file is not specified, the password for the .pfx file will be the same as the password for .pvk file.

<span id="_f"></span><span id="_F"></span>**/f**  
Configures Pvk2Pfx to overwrite a .pfx file, if one exists that has the same name as that specified by the **-pfx** switch.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

If the **-pfx** *pfxfilename.pfx* switch is not supplied, pvk2pfx ignores the **-po** *password* switch and the **-f** switch, and displays a wizard that prompts the user for the name of the .pfx file and its corresponding password.

In order to use the [**SignTool**](signtool.md) tool to sign drivers using a SPC in a manner that complies with the [kernel-mode code signing policy](https://msdn.microsoft.com/library/windows/hardware/ff548231), the SPC information must be added to the Personal certificate store on the local computer that signs the drivers. For information about how to add the SPC information to the Personal certificate store, see [Software Publisher Certificate](https://msdn.microsoft.com/library/windows/hardware/ff552299).

A 32-bit version of the Pvk2Pfx tool is located in the bin\\x86 folder of the WDK. A 64-bit version of the tool is located in the bin\\x64 of the WDK. For example, on an x64-based computer running Windows 10, the path is C:\\Program Files (x86)\\Windows Kits\\10\\bin\\x64.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The following command generates the .pfx file Mypfxfile.pfx from Mypvkfile.pvk and Myspcfile.spc. The command supplies the password mypassword for the .pvk file, which becomes the password for the .pfx file Mypfxfile.pfx. If there is an existing file named Mypfxfile.pfx, the **-f** switch configures the Pvk2Pfx tool to replace the existing file with a new file.

``` syntax
pvk2pfx -pvk mypvkfile.pvk -pi mypassword -spc myspcfile.spc -pfx mypfxfile.pfx -f
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Pvk2Pfx%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




