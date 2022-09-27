---
title: Referencing locales
description: Provides information about referencing locales.
keywords:
- Unidrv, referencing locales
- GPD files WDK Unidrv, referencing locales
- referencing locales
- locale referencing WDK Unidrv
- Unidrv WDK print
ms.date: 09/08/2022
---

# Referencing locales

## Using GPD files

GPD files can reference a system's locale. Typically, locale identifiers are used within \*Switch statements, where parameters such as default paper sizes and resource DLLs can be specified in a locale specific manner.

To reference locale information, the GPD file must contain an \*Include statement that includes the file locale.gpd, which is included in the with the Windows Driver Kit (WDK), as follows:

```cpp
*Include: locale.gpd
```

This GPD file defines a feature named "Locale", and defines options for many locales. (Refer to the file to see which locales are defined.) Following is an example usage of these locale options. The example bases the default paper size on the locale.

```cpp
*Feature: PaperSize
{
...
    Option: A4
    {
    }
    ...
*switch: Locale
{
    *case: English_United_States
    {
        *DefaultOption: Letter
    }
    *case: English_United_Kingdom
    {
        *DefaultOption: A4
    }
    *default:
    {
        *DefaultOption: Letter
    }
} *% End of switch
} *% End of Feature: PaperSize
```

At run time, Unidrv determines the system's default locale by calling [**GetSystemDefaultLCID**](/windows/win32/api/winnls/nf-winnls-getsystemdefaultlcid). When a printer is installed, the GPD parser reads the printer's GPD file and uses information within the \*Case statement associated with the default locale. Note that if the system's locale is changed after the printer is installed, locale-based options are not changed.

Here is another example, which selects a resource DLL based on the locale. The resource DLL can contain locale-specific resources, such as display strings.

```cpp
*switch: Locale
{
    *case: English_United_States
    {
        *ResourceDLL: english.dll
    }
    *case: German_Standard
    {
        *ResourceDLL: german.dll
    }
    *default:
    {
        *ResourceDLL: english.dll
    }
}
```

## Setting default paper size by locale

You might want to have your driver assign the default paper size, either metric or non-metric, based upon the user's geographic location.

The following algorithm retrieves the default system locale and then uses country/region codes to determine whether the system locale represents a country that typically uses metric or non-metric paper sizes. With this information, your driver can set the default paper size appropriately, such as A4 for countries that use the metric system and Letter size for countries that don't.

1. Use the [GetLocaleInfo](/previous-versions//ms776270(v=vs.85)) function to retrieve the default system locale. Use LOCALE_SYSTEM_DEFAULT for the first parameter, *Locale*, and LOCALE_ICOUNTRY for the second parameter, *LCType*.

1. Use the default system locale obtained from **GetLocaleInfo** to determine metric or non-metric paper size.
    - Non-metric if default system locale is:

        - CTRY_UNITED_STATES, or

        - CTRY_CANADA, or

        - Greater than or equal to 50, but less than 60 and not CTRY_BRAZIL, or

        - Greater than or equal to 500, but less than 600

    - Metric otherwise.
