---
title: How do I create custom WPP extended format specification strings
description: How do I create custom WPP extended format specification strings
ms.assetid: 6c4c47c6-71b2-48a0-bab3-8498029b8244
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I create custom WPP extended format specification strings?


You create custom WPP extended format specification strings by using the DEFINE\_CPLX\_TYPE macro. For more information about how to use this macro, see [What is the syntax of the complex types definition?](what-is-the-syntax-of-the-complex-types-definition-.md).

This topic provides examples that show you how to do the following:

- [Trace fixed-length strings through custom WPP extended format specification strings](#trace-fixed-length-strings-through-custom-wpp-extended-format-specification-strings)

- [Trace variable-length strings through custom WPP extended format specification strings](#trace-variable-length-strings-through-custom-wpp-extended-format-specification-strings)

Each of these examples shows the use of a custom WPP configuration file for the definition of the DEFINE\_CPLX\_TYPE macro. In these examples, the configuration file is named LocalWpp.ini. For more information about how to use custom WPP configuration files, see [How do you define custom data types?](how-do-you-define-custom-data-types-.md).

## Trace fixed-length strings through custom WPP extended format specification strings

This example shows how to trace Internet Protocol version 6 (IPv6) network addresses by using a custom WPP extended format specification string. IPv6 network addresses, as defined by the in6\_addr structure, have a fixed-length length of 16 bytes.

In this example, a complex data type (IPV6ADDR) is defined, which can then be used as the %!IPV6ADDR! format specification string in your source code.

To create the IPV6ADDR complex data type, add the following statements to the LocalWpp.ini configuration file:

1.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>DEFINE_CPLX_TYPE(IPV6ADDR, WPP_LOGIPV6, in6_addr *, ItemIPV6Addr, &quot;s&quot;, _IPV6_, 0, 1);</code></pre></td>
    </tr>
    </tbody>
    </table>

    This statement uses the DEFINE\_CPLX\_TYPE macro to define the complex type (IPV6ADDR) along with its attributes, such as its argument type (in6\_addr \*) and size (16).

    The statement also specifies the name of a helper macro (WPP\_LOGIPV6) that is used by the WPP preprocessor when it parses an IPV6ADDR complex type in the source code of your [trace provider](trace-provider.md).

2.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>WPP_FLAGS(-DWPP_LOGIPV6(x) WPP_LOGPAIR( (16), (x)));</code></pre></td>
    </tr>
    </tbody>
    </table>

    This statement defines the helper macro that is used to format the length/address pair of the IPV6 argument when it is passed to the [TraceMessage](http://go.microsoft.com/fwlink/p/?linkid=179214) function.

In Visual Studio, open the properties page for your project. Under **WPP Tracing**, **File Options**, specify LocalWpp.ini as the **Additional Configuration file**. See [WPP Preprocessor](wpp-preprocessor.md) for more information.

The following sample source code shows how your [trace provider](trace-provider.md) can trace IPv6 network addresses by using the %!IPV6ADDR! format specification string:

```
struct in6_addr IPAddressV6 = {0};
DoTraceMessage(Noise, "IN6_ADDR  = %!IPV6ADDR!", &IPAddressV6);
```

**Note**  You can create a complex type (MACADDR) for tracing fixed-length media access control (MAC) addresses. This complex type can be specified by following the procedure that was used for the IPV6ADDDR complex type.

 

## Trace variable-length strings through custom WPP extended format specification strings

This example shows how to trace variable-length buffers of data by using a custom WPP extended format specification string.

In this example, a complex data type (HEXDUMP) is defined which can then be used as the %!HEXDUMP! format specification string in your source code.

To create the HEXDUMP complex data type, add the following statements to the LocalWpp.ini configuration file:

1.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>DEFINE_CPLX_TYPE(HEXDUMP, WPP_LOGHEXDUMP, const xstr_t&, ItemHEXDump,&quot;s&quot;, _HEX_, 0, 2);</code></pre></td>
    </tr>
    </tbody>
    </table>

    This statement uses the DEFINE\_CPLX\_TYPE macro to define the complex type (HEXDUMP) along with its attributes, such as its argument type (const xstr\_t&) and the number of parameters that are passed to **TraceMessage** (2). Because this complex type is to be used for variable-length data, the macro's **Size** element is set to zero.

    The statement also specifies the name of a helper macro (WPP\_LOGHEXDUMP) that is used by the WPP preprocessor when it parses a HEXDUMP complex type in the source code of your [trace provider](trace-provider.md).

2.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>struct xstr_t {
       CHAR * _buf;
       short _len;
       xstr_t(__in_ecount(len) char *buf, short len):_buf(buf),_len(len) {}
    };</code></pre></td>
    </tr>
    </tbody>
    </table>

    This statement defines a structure that is used to save the length and address of a variable-length buffer. This structure is initialized in the LOG\_LENSTR macro, and is local to each invocation of [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) in which the HEXDUMP complex type is used within the *FormatString* parameter.

3.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>WPP_FLAGS(-DLOG_LENSTR(len,str)=xstr_t(str,len));</code></pre></td>
    </tr>
    </tbody>
    </table>

    This statement defines the macro that is used to initialize an xstr\_t structure for the variable-length buffer. You must use this macro to pass the variable-length buffer in the *VariableList* parameter of [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918).

4.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>WPP_FLAGS(-DWPP_LOGHEXDUMP(x) WPP_LOGPAIR(2,&(x)._len) WPP_LOGPAIR((x)._len, (x)._buf));</code></pre></td>
    </tr>
    </tbody>
    </table>

    This statement defines the helper macro that is used to format the length/address pairs of the variable-length buffer argument when it is passed to the [TraceMessage](http://go.microsoft.com/fwlink/p/?linkid=179214) function.

    Variable-length arguments require two length/address pairs. As a result, the WPP\_LOGHEXDUMP macro defines two calls to WPP\_LOGPAIR in the following way:

    -   The first call to WPP\_LOGPAIR passes the size of the variable-length buffer.
    -   The second call to WPP\_LOGPAIR passes the address of the buffer itself.

    **Note**  This macro requires that an xstr\_t structure has been initialized for the variable-length buffer by a call to LOG\_LENSTR. As a result, you must pass the variable-length buffer to [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) through the LOG\_LENSTR macro.

     

In Visual Studio, open the properties page for your project. Under **WPP Tracing**, **File Options**, specify LocalWpp.ini as the **Additional Configuration file**. See [WPP Preprocessor](wpp-preprocessor.md) for more information.

The following sample source code shows how your [trace provider](trace-provider.md) can trace a buffer of data by using the %!HEXDUMP! format specification string:

```
CHAR HexDump[1024] = {0, 1, 2, 3, 4, 5, 6, 7} ;
DoTraceMessage(Noise, "HEXDUMP: %!HEXDUMP! ", LOG_LENSTR(sizeof(HexDump),(PCHAR)HexDump));
```

**Note**  You can create a complex type (HEXBYTES) for tracing variable-length buffers. This complex type can be specified by following the procedure that was used for the HEXDUMP complex type. 





