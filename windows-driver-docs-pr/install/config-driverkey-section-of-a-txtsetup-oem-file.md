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
---

# Config.DriverKey Section of a TxtSetup.oem File


A **Config.***DriverKey* section specifies values to be set in the registry for particular component options. Windows automatically creates the required values in the **Services\\***DriverKey* key. Use this section to specify additional keys to be created under **Services\\***DriverKey* and values under **Services\\***DriverKey* and **Services\\***DriverKey*\\*subkey\_name*.

``` syntax
[Config.DriverKey]
value = subkey_name,value_name,value_type,value
...
```

<a href="" id="subkey-name"></a>*subkey\_name*  
Specifies the name of a key under the **Services\\***DriverKey* tree where Windows places the specified value. Windows creates the key if it does not exist.

If *subkey\_name* is the empty string (""), the value is placed under the **Services\\***DriverKey*.

The *subkey\_name* can specify more than one level of subkey, such as "subkey1\\subkey2\\subkey3".

<a href="" id="value-name"></a>*value\_name*  
Specifies the name of the value to be set.

<a href="" id="value-type"></a>*value\_type*  
Specifies the type of the registry entry. The *value\_type* can be one of the following:

<a href="" id="reg-dword"></a>REG\_DWORD  
One *value* is allowed; it must be a string containing up to eight hexadecimal digits.

For example:

``` syntax
value = parameters,NumberOfButtons,REG_DWORD,2
```

<a href="" id="reg-sz-or-reg-expand-sz"></a>REG\_SZ or REG\_EXPAND\_SZ  
One *value* is allowed; it is interpreted as the null-terminated string to be stored.

For example:

``` syntax
value = parameters,Description,REG_SZ,"This is a text string"
```

<a href="" id="reg-binary"></a>REG\_BINARY  
One *value* is allowed; it is a string of hex digits, each pair of which is interpreted as a byte value.

For example (stores the byte stream 00,34,ec,4d,04,5a):

``` syntax
value = parameters,Data,REG_BINARY,0034eC4D045a
```

<a href="" id="reg-multi-sz"></a>REG\_MULTI\_SZ  
Multiple *value* arguments are allowed; each is interpreted as a component of the MULTI\_SZ string.

For example:

``` syntax
value = parameters,Strings,REG_MULTI_SZ,String1,"String 2",string3
```

<a href="" id="value"></a>*value*  
Specifies the value; its format depends on *value\_type*.

The following example shows a **Config.***DriverKey* section:

``` syntax
; ...
[Config.OEMSCSI]
value = parameters\PnpInterface,5,REG_DWORD,1
; ...
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Config.DriverKey%20Section%20of%20a%20TxtSetup.oem%20File%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




