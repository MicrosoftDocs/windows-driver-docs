---
title: What is the syntax of the complex types definition
description: What is the syntax of the complex types definition
ms.assetid: c378839a-3714-4b4e-94a6-d3e1dcf8a610
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What is the syntax of the complex types definition?


Event Tracing for Windows (ETW) defines several simple and complex types for use in the tracing functions. These types are declared in the Defaultwpp.ini file. However, you can create your own custom configuration file and direct WPP to use it.

The format of the complex data type, DEFINE\_CPLX\_TYPE, is as follows:

```
DEFINE_CPLX_TYPE(TypeName, HelperMacroName, ArgumentType, WppMofType,"WppMofFormat", TypeSignature, Priority, Slots);
```

For example:

```
DEFINE_CPLX_TYPE(.*ls, WPP_LOGXWCS, const xwcs_t&, ItemPWString,"s", _xwcs_t_, 0, 2);
```

### <span id="format_elements"></span><span id="FORMAT_ELEMENTS"></span>Format Elements

<span id="TypeName"></span><span id="typename"></span><span id="TYPENAME"></span>*TypeName*  
WPP uses this field to identify the complex type. For example, **.\*ls**.

<span id="HelperMacroName"></span><span id="helpermacroname"></span><span id="HELPERMACRONAME"></span>*HelperMacroName*  
A helper macro that converts an argument into a variable-length array in the format of a length/address pair. This format is required by the **TraceMessage** function for each of the entries in its variable argument list.

To format the argument properly, you must use the [**WPP\_LOGPAIR**](https://msdn.microsoft.com/library/windows/hardware/ff556197) macro in the definition of the helper macro, as shown in the following example:

```
#define HelperMacroName(x) WPP_LOGPAIR(length, x)
```

**Note**  Depending on the tracing logic that you want to implement, you may need to define the macro by using multiple WPP\_LOGPAIR macros.

 

<span id="Argument_Type"></span><span id="argument_type"></span><span id="ARGUMENT_TYPE"></span>*Argument Type*  
Indicates the value that arguments of *TypeName* type can accept. For example, **const xwcs\_t&**.

<span id="WppMofType"></span><span id="wppmoftype"></span><span id="WPPMOFTYPE"></span>*WppMofType*  
Specifies a Managed Object Format (MOF) type that is recognized by the WPP preprocessor

<span id="WppMofFormat"></span><span id="wppmofformat"></span><span id="WPPMOFFORMAT"></span>*WppMofFormat*  
Specifies a format specifier, such as **"s"**, that is recognized by the WPP preprocessor.

<span id="TypeSignature"></span><span id="typesignature"></span><span id="TYPESIGNATURE"></span>*TypeSignature*  
A string appended to the function name to associate it with the complex type. There must be a single character or multiple characters between underscores. For example, **\_xwcs\_t\_**.

<span id="Priority"></span><span id="priority"></span><span id="PRIORITY"></span>*Priority*  
This element is reserved and must be set to zero.

<span id="Slots"></span><span id="slots"></span><span id="SLOTS"></span>*Slots*  
Specifies the maximum number of variable-length parameters that the WPP preprocessor passes to the [TraceMessage](http://go.microsoft.com/fwlink/p/?linkid=179214) function for this complex type. This format element is optional. WPP uses a default value of 1 if this element is not specified.

### <span id="example"></span><span id="EXAMPLE"></span>Example

To define a complex type, do the following:

1.  Create a local configuration file. This file should contains the DEFINE\_CPLX\_TYPE macro that defines the complex type.

2.  Specify the local configuration file to the [WPP Preprocessor](wpp-preprocessor.md). Open the project properties. Under **WPP Tracing**, **File Options**, use the **Additional Configuration file** field to specify the name of the configuration file (**-ini** parameter). Be sure to enable WPP tracing by setting **Run WPP** to **Yes**. See WPP Preprocessor for more information.

For example, you can create a local configuration file (Localwpp.ini) that defines a complex type named **.\*ls**. You define the complex type in the following way:

```
DEFINE_CPLX_TYPE(.*ls, WPP_LOGXWCS, const xwcs_t&, ItemPWString,"s", _xwcs_t_, 0, 2);
```

Then, when WPP sees a type **.\*ls**, such as in:

```
printf("my string is %.*ls", value);
```

WPP generates the following staging function (where **SF** represents "staging function"):

```
WPP_SF__xwcs_t_(..., const xwcs_t& a1) {
    TraceMessage(..., WPP_LOGXWCS(a1) 0);
}
```

WPP then generates a MOF entry, such as in the following string, where the **.\*ls** type name is replaced with the appropriate MOF format, **%s**.

```
"my string is %s"
{
    Value, ItemPWString
}
```

It also generates a structure for the type, such as

```
struct xwcs_t {
      WCHAR*    _buf;
      short     _len;
      xwcs_t(short buf, short len):_buf(buf),_len(len){}
};
```

Now, add a macro to combine the data types into a string of type **xwstr\_t**, as follows:

```
#define WPP_LOGXWCS(x) WPP_LOGPAIR(2, &(x)._len) WPP_LOGPAIR((x)._len, (x)._buf)
```

where **ItemPWString** is a counted Unicode string type recognized by WPP. The length is specified as 2 bytes.

When ETW interprets the WPP\_LOGXWCS definition, it puts a 2-byte string into a buffer the first [**WPP\_LOGPAIR**](https://msdn.microsoft.com/library/windows/hardware/ff556197) macro is interpreted. ETW then copies all the bytes of the string into a buffer when ETW interprets the second WPP\_LOGPAIR macro,

Because you specified the length separate from the data, WPP\_LOGXWCS consumes two slots of [TraceMessage](http://go.microsoft.com/fwlink/p/?linkid=179214). Therefore, the number **2** is the eighth argument.

When calling the [WPP Preprocessor](wpp-preprocessor.md), use the **Ignore Exclamation Marks** option (**-noshrieks**). This helps WPP to recognize a complex type that has a name that is not enclosed in exclamation marks (!), also known as "shrieks."

For a complete list of the WPP Tracing options and information about how to set them from the project property page, see [WPP Preprocessor](wpp-preprocessor.md).

 

 





