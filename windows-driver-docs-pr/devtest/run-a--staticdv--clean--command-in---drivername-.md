---
title: Run a "staticdv /clean" command in drivername
description: Run a \ 0034;staticdv /clean \ 0034; command in drivername
ms.assetid: 179ade54-625f-427e-b680-f9814c41808f
---

# Run a "staticdv /clean" command in :&lt;drivername&gt;


SDV reports this error when you submit a command to verify a driver before deleting the files from a previous verification.

When SDV verifies a driver, it creates files in which it records the results of the verification. It uses these files to create the display in the Static Driver Verifier Report. If these previous versions of these files already exist in the directory, SDV does not overwrite the files. Instead, it displays this message asking you to delete the files intentionally.

To eliminate the error, use the **/clean** command option, or click **Clean** in Static Driver Verifier. This deletes the files from the previous verification.

If the approved flag is set to true in the Sdv-map.h file (Approved=true), SDV retains the Sdv-map.h file so that you do not have to scan the driver entry routine again or approve the file contents.

For more information about **/clean** and other commands, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Run%20a%20"staticdv%20/clean"%20command%20in%20:<drivername>%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




