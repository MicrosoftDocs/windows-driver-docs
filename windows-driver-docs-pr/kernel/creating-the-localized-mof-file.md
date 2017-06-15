---
title: Creating the Localized MOF File
author: windows-driver-content
description: Creating the Localized MOF File
MS-HAID:
- 'WMI\_eb53b6fc-39df-4501-9d59-f206381d12af.xml'
- 'kernel.creating\_the\_localized\_mof\_file'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1cc99e43-b09a-445d-abb6-4a3d73b6d7ed
keywords: ["MOF files WDK WMI", "localizing MOF files", "property qualifiers WDK WMI", "amended classes WDK WMI", "multiple MOF files WDK WMI", "languages WDK WMI"]
---

# Creating the Localized MOF File


## <a href="" id="ddk-creating-the-localized-mof-file-kg"></a>


On Windows XP and later versions of the operating system, drivers localize a WMI schema by making an *amended* version of each class. An amended version of a class updates property qualifiers that depend on the locale.

An amended version of a class has the same format as a class declaration, preceded by the **amendment** qualifier. The amended class declaration also includes a **locale(**0x*XXX***)** qualifier, where *XXX* specifies the locale identifier (LCID) for the locale.

The amended declaration includes the modified property declarations. Each localized property qualifier has the **:amended** modifier attached to it. For example, the localized version of **Description("***a description string***")** would be **Description("***localized description string***"):amended**.

Here is an example of a declaration of the basic class, followed by its amendment for American English.

```
[guid(xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx)]
class MyClass
{
    [key] sint32 KeyProp;
    string Name;
    uint64 Timestamp;
}

[amendment, locale(0x409)
 Description("Localized version of MyClass for American English"):amended]

class MyClass
{
    [DisplayName("Key Property"):amended,
     Description("The description of KeyProp"):amended]
    sint32 KeyProp;

    [DisplayName("User Name"):amended,
     Description("The description of Name"):amended]
    string Name;
}
```

Only the properties that have been modified need to be included in the amended class. The class and property names cannot be localized. Only property qualifiers can be localized.

Localized classes are organized in child namespaces of the namespace containing the original class. Classes for a given locale are found in the MS\_*XXX* child namespace, where *XXX* represents the hexadecimal LCID for that locale. For example, drivers are in the \\root\\wmi namespace by default. An amended class, localized for American English, is found in the \\root\\wmi\\MS\_409 namespace.

For more information about WMI localization, see the [WMI international support](http://go.microsoft.com/fwlink/p/?linkid=8774) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Creating%20the%20Localized%20MOF%20File%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


