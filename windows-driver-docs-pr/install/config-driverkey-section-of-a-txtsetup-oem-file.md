---
title: Config.DriverKey Section of a TxtSetup.oem File
description: A Config.DriverKey section specifies values to be set in the registry for particular component options.
ms.assetid: 0b9fe0ff-2b97-416e-8ced-62b59eabf94a
keywords: ["Config.DriverKey Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
api_name:
- Config.DriverKey Section of a TxtSetup.oem File
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Config.DriverKey Section of a TxtSetup.oem File


A **Config.**<em>DriverKey</em> section specifies values to be set in the registry for particular component options. Windows automatically creates the required values in the **Services\\**<em>DriverKey</em> key. Use this section to specify additional keys to be created under **Services\\**<em>DriverKey</em> and values under **Services\\**<em>DriverKey</em> and **Services\\**<em>DriverKey</em>\\*subkey_name*.

``` syntax
[Config.DriverKey]
value = subkey_name,value_name,value_type,value
...
```

<a href="" id="subkey-name"></a>*subkey_name*  
Specifies the name of a key under the **Services\\**<em>DriverKey</em> tree where Windows places the specified value. Windows creates the key if it does not exist.

If *subkey_name* is the empty string (""), the value is placed under the **Services\\**<em>DriverKey</em>.

The *subkey_name* can specify more than one level of subkey, such as "subkey1\\subkey2\\subkey3".

<a href="" id="value-name"></a>*value_name*  
Specifies the name of the value to be set.

<a href="" id="value-type"></a>*value_type*  
Specifies the type of the registry entry. The *value_type* can be one of the following:

<a href="" id="reg-dword"></a>REG_DWORD  
One *value* is allowed; it must be a string containing up to eight hexadecimal digits.

For example:

``` syntax
value = parameters,NumberOfButtons,REG_DWORD,2
```

<a href="" id="reg-sz-or-reg-expand-sz"></a>REG_SZ or [REG_EXPAND_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)  
One *value* is allowed; it is interpreted as the null-terminated string to be stored.

For example:

``` syntax
value = parameters,Description,REG_SZ,"This is a text string"
```

<a href="" id="reg-binary"></a>REG_BINARY  
One *value* is allowed; it is a string of hex digits, each pair of which is interpreted as a byte value.

For example (stores the byte stream 00,34,ec,4d,04,5a):

``` syntax
value = parameters,Data,REG_BINARY,0034eC4D045a
```

<a href="" id="reg-multi-sz"></a>REG_MULTI_SZ  
Multiple *value* arguments are allowed; each is interpreted as a component of the MULTI_SZ string.

For example:

``` syntax
value = parameters,Strings,REG_MULTI_SZ,String1,"String 2",string3
```

<a href="" id="value"></a>*value*  
Specifies the value; its format depends on *value_type*.

The following example shows a **Config.**<em>DriverKey</em> section:

``` syntax
; ...
[Config.OEMSCSI]
value = parameters\PnpInterface,5,REG_DWORD,1
; ...
```

 

 





