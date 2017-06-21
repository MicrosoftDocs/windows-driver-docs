---
title: Building and Deploying the Localized MOF File
author: windows-driver-content
description: Building and Deploying the Localized MOF File
ms.assetid: 3a741dc6-a789-44e1-9d68-cdb41b7161ed
keywords: ["MOF files WDK WMI", "localizing MOF files", "MUI versions WDK WMI", "master MOF files WDK WMI", "languages WDK WMI"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Building and Deploying the Localized MOF File


## <a href="" id="ddk-building-and-deploying-the-localized-mof-file-kg"></a>


International versions of Windows XP and later versions of the operating system come in two flavors — single-language (localized) versions, and Multilanguage User Interface (MUI) versions. An MUI version of Windows can support several languages simultaneously.

Drivers that are deployed on a localized version of Windows should contain a MOF resource that contains the language-neutral version of all the classes, as well as the localized language amendment and the American English language amendment.

On an MUI version of Windows, the driver image itself should contain the language-neutral and American English versions of the WMI classes. For each additional language supported, a resource-only image can be placed in the %windir%\\system32\\drivers\\MUI\\*langid* directory, where *langid* is the LCID of the for the locale.

Optionally, the driver image itself can contain every language supported.

If a language is not supported by one of these mechanisms, the English language version is used.

### Building Distinct MOF Files For Each Language

Driver writers can use one master MOF text file to contain the basic class, and all of its amendments.

You can use the [MOF compiler](compiling-a-driver-s-mof-file.md) to generate a file containing the language-neutral classes as well as a file to contain the amended classes for a particular language.

```
mofcomp -amendment:namespace [ -MOF:mof] [ -MFL:mfl] masterfile
```

The *namespace* parameter is of the form MS\_*XXX*, where *XXX* is the LCID for the locale to be generated. The mof file created contains the language-neutral classes, and the mfl file created contains the amended classes.

When building your driver on NT-based operating systems, you can merge the two files by using the copy command. On Windows 98/Me, the copy command does not correctly append Unicode files, but the following command can be used.

```
wmimofck localizedfile -ymof -zmfl
```

You can combine any number of languages into a single text file.

The localized file can then be compiled into a binary file by the same method as for the MOF files that have not been localized:

```
mofcomp -B:binaryfile localizedfile
```

For a single-language version of Windows, drivers attach the binary MOF as a resource to the driver image. See [Compiling a Driver's MOF File](compiling-a-driver-s-mof-file.md) for details.

On an MUI system, the driver image itself must be built for American English. For each additional language, install each localized binary MOF file as a resource in a separate image file in the appropriate %windir%\\system32\\drivers\\MUI\\*langid* directory, where *langid* is the hexadecimal LCID for the locale (for example, 409 for American English). The file name must be either *drivername.sys* or *drivername.sys*.mui, where *drivername.sys* is the name of the driver binary.

### Building One MOF File for All Supported Languages

If the driver image will contain every supported language, there is a simpler way to build a MOF file supporting every language. By using **\#pragma** directives in the MOF text file, drivers can also combine all of the amended classes in one binary. Since each localization exists in a distinct namespace, they can safely be combined in a single binary.

When writing the combined MOF text file, driver writers must precede each amended class declaration with a **\#pragma** directive as follows

```
#pragma namespace ("namespace")
```

where `namespace` is the correct namespace for the declaration. For example, the amended class declaration for American English must be preceded with a declaration of the form:

```
#pragma namespace ("\\\\.\\root\\wmi\\ms_409")
```

For example, you declare a class and its amendments as follows.

```
#pragma namespace ("\\\\.\\root\\wmi)

[guid(xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx)]
class MyClass 
{
}

#pragma namespace(\\\\.\\root\\wmi\\ms_409)
[amendment, locale(0x407)]
class MyClass
{
}
```

Using this approach, building the binary MOF file is identical to the nonlocalized approach. See [Compiling a Driver's MOF File](compiling-a-driver-s-mof-file.md) for details.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Building%20and%20Deploying%20the%20Localized%20MOF%20File%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


