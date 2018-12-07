---
title: Creating the Localized MOF File
description: Creating the Localized MOF File
ms.assetid: 1cc99e43-b09a-445d-abb6-4a3d73b6d7ed
keywords: ["MOF files WDK WMI", "localizing MOF files", "property qualifiers WDK WMI", "amended classes WDK WMI", "multiple MOF files WDK WMI", "languages WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating the Localized MOF File





On Windows XP and later versions of the operating system, drivers localize a WMI schema by making an *amended* version of each class. An amended version of a class updates property qualifiers that depend on the locale.

An amended version of a class has the same format as a class declaration, preceded by the **amendment** qualifier. The amended class declaration also includes a <strong>locale(</strong>0x<em>XXX</em>**)** qualifier, where *XXX* specifies the locale identifier (LCID) for the locale.

The amended declaration includes the modified property declarations. Each localized property qualifier has the **:amended** modifier attached to it. For example, the localized version of **Description("**<em>a description string</em>**")** would be **Description("**<em>localized description string</em>**"):amended**.

Here is an example of a declaration of the basic class, followed by its amendment for American English.

```cpp
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

 

 




