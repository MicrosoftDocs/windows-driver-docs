---
title: x (Examine Symbols)
description: The x command displays the symbols in all contexts that match the specified pattern.
ms.assetid: 8c71c2ca-4a9d-43e4-91b3-f05b5475316d
keywords: ["x (Examine Symbols) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- x (Examine Symbols)
api_type:
- NA
ms.localizationpriority: medium
---

# x (Examine Symbols)


The **x** command displays the symbols in all contexts that match the specified pattern.

```dbgcmd
x [Options] Module!Symbol 
x [Options] *
```

## <span id="ddk_cmd_examine_symbols_dbg"></span><span id="DDK_CMD_EXAMINE_SYMBOLS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies symbol searching options. You can use one or more of the following options:

<span id="_0"></span>**/0**  
Displays only the address of each symbol.

<span id="_1"></span>**/1**  
Displays only the name of each symbol.

<span id="_2"></span>**/2**  
Displays only the address and name of each symbol (not the data type).

<span id="_D"></span><span id="_d"></span>**/D**  
Displays the output using [Debugger Markup Language](debugger-markup-language-commands.md).

<span id="_t"></span><span id="_T"></span>**/t**  
Displays the data type of each symbol, if the data type is known.

<span id="_v"></span><span id="_V"></span>**/v**  
Displays the symbol type (local, global, parameter, function, or unknown) of each symbol. This option also displays the size of each symbol. The size of a function symbol is the size of the function in memory. The size of other symbols is the size of the data type that the symbol represents. Size is always measured in bytes and displayed in hexadecimal format.

<span id="_s_Size"></span><span id="_s_size"></span><span id="_S_SIZE"></span>**/s** *Size*  
Display only those symbols whose size, in bytes, equals the value of *Size*. The *Size* of a function symbol is the size of the function in memory. The *Size* of other symbols is the size of the data type that the symbol represents. Symbols whose size cannot be determined are always displayed. *Size* must be a nonzero integer.

<span id="_q"></span><span id="_Q"></span>**/q**  
Displays symbol names in quoted format.

<span id="_p"></span><span id="_P"></span>**/p**  
Omits the space before the opening parenthesis when the debugger displays a function name and its arguments. This kind of display can make it easier if you are copying function names and arguments from the **x** display to another location.

<span id="_f"></span><span id="_F"></span>**/f**  
Displays the data size of a function.

<span id="_d"></span><span id="_D"></span>**/d**  
Displays the data size of data.

<span id="_a"></span><span id="_A"></span>**/a**  
Sorts the display by address, in ascending order.

<span id="_A"></span><span id="_a"></span>**/A**  
Sorts the display by address, in descending order.

<span id="_n"></span><span id="_N"></span>**/n**  
Sorts the display by name, in ascending order.

<span id="_N"></span><span id="_n"></span>**/N**  
Sorts the display by name, in descending order.

<span id="_z"></span><span id="_Z"></span>**/z**  
Sorts the display by size, in ascending order.

<span id="_Z"></span><span id="_z"></span>**/Z**  
Sorts the display by size, in descending order.

<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module to search. This module can be an .exe, .dll, or .sys file. *Module* can contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies a pattern that the symbol must contain. *Symbol* can contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

Because this pattern is matched to a symbol, the match is not case sensitive, and a single leading underscore (\_) represents any quantity of leading underscores. You can add spaces within *Symbol*, so that you can specify symbol names that contain spaces (such as "operator new" or "Template&lt;A, B&gt;") without using wildcard characters.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The following command finds all of the symbols in MyModule that contain the string "spin".

```dbgcmd
0:000> x mymodule!*spin* 
```

The following command quickly locates the "DownloadMinor" and "DownloadMajor" symbols in MyModule.

```dbgcmd
0:000> x mymodule!downloadm??or 
```

You can also show all symbols in the MyModule by using the following command.

```dbgcmd
0:000> x mymodule!* 
```

The preceding commands also force the debugger to reload symbol information from MyModule. If you want to reload the symbols in the module with a minimal display, use the following command.

```dbgcmd
0:000> x mymodule!*start* 
```

A few symbols always contain the string "start". Therefore, the preceding command always displays some output to verify that the command works. But the preceding command avoids the excessive display length of **x mymodule!\\***.

The display shows the starting address of each symbol and the full symbol name. If the symbol is a function name, the display also includes a list of its argument types. If the symbol is a global variable, its current value is displayed.

There is one other special case of the **x** command. To display the addresses and names of all local variables for the current context, use the following command.

```dbgcmd
0:000> x * 
```

**Note**   In most cases, you cannot access local variables unless private symbols have been loaded. For more information about this situation, see [dbgerr005: Private Symbols Required](dbgerr005--private-symbols-required.md). To display the values of local variables, use the [**dv (Display Local Variables)**](dv--display-local-variables-.md) command.

 

The following example illustrates the **/0**, **/1**, and **/2** options.

```dbgcmd
0:000:x86> x /0 MyApp!Add*
00b51410          
00b513d0 
      
0:000:x86> x /1 MyApp!Add*
MyApp!AddThreeIntegers
MyApp!AddTwoIntegers

0:000:x86> x /2 MyApp!Add*
00b51410          MyApp!AddThreeIntegers
00b513d0          MyApp!AddTwoIntegers
```

The **/0**, **/1**, and **/2** options are useful if you want to use the output of the **x** command as input to the [**.foreach**](-foreach.md) command.

```dbgcmd
.foreach ( place { x /0 MyApp!*MySym*} ) { .echo ${place}+0x18 }
```

The following example demonstrates the switch **/f** when used to filter functions on the module notepad.exe.

```dbgcmd
0:000> x /f /v notepad!*main*
prv func   00000001`00003340  249 notepad!WinMain (struct HINSTANCE__ *, struct HINSTANCE__ *, char *, int)
prv func   00000001`0000a7b0   1c notepad!WinMainCRTStartup$filt$0 (void)
prv func   00000001`0000a540  268 notepad!WinMainCRTStartup (void)
```

When you use the **/v** option, the first column of the display shows the symbol type (local, global, parameter, function, or unknown). The second column is the address of the symbol. The third column is the size of the symbol, in bytes. The fourth column shows the module name and symbol name. In some cases, this display is followed by an equal sign (=) and then the data type of the symbol. The source of the symbol (public or full symbol information) is also displayed.

```dbgcmd
kd> x /v nt!CmType*
global 806c9e68    0 nt!CmTypeName = struct _UNICODE_STRING []
global 806c9e68  150 nt!CmTypeName = struct _UNICODE_STRING [42]
global 806c9e68    0 nt!CmTypeName = struct _UNICODE_STRING []
global 805bd7b0    0 nt!CmTypeString = unsigned short *[]
global 805bd7b0   a8 nt!CmTypeString = unsigned short *[42]
```

In the preceding example, the size is given in hexadecimal format, while the data type is given in decimal format. Therefore, in the last line of the preceding example, the data type is an array of 42 pointers to unsigned short integers. The size of this array is 42\*4 = 168, and 168 is displayed in hexadecimal format as 0xA8.

You can use the **/s***Size* option to display only those symbols whose size, in bytes, is a certain value. For example, you can restrict the command in the preceding example to symbols that represent objects whose size is 0xA8.

```dbgcmd
kd> x /v /s a8 nt!CmType*
global 805bd7b0   a8 nt!CmTypeString = unsigned short *[42]
```

**Working With Data Types**

The **/t** option causes the debugger to display information about each symbol's data type. Note that for many symbols, this information is displayed even without the **/t** option. When you use **/t**, such symbols have their data type information displayed twice.

```dbgcmd
0:001> x prymes!__n*
00427d84 myModule!__nullstring = 0x00425de8 "(null)"
0042a3c0 myModule!_nstream = 512
Type information missing error for _nh_malloc
004021c1 myModule!MyStructInstance = struct MyStruct
00427d14 myModule!_NLG_Destination = <no type information>

0:001> x /t prymes!__n*
00427d84 char * myModule!__nullstring = 0x00425de8 "(null)"
0042a3c0 int myModule!_nstream = 512
Type information missing error for _nh_malloc
004021c1 struct MyStruct myModule!MyStructInstance = struct MyStruct
00427d14 <NoType> myModule!_NLG_Destination = <no type information>
```

The x command will display an instance of a type.

```dbgcmd
0:001> x foo!MyClassInstance
00f4f354          foo!MyClassInstance = 0x00f78768
```

The x command does not display anything based on just the name of a type.

```dbgcmd
0:001> x foo!MyClass
0:001>
```

To display type information using the name of a type, consider using [**dt (Display Type)**](dt--display-type-.md), it provides information for both types and instances of types:

```dbgcmd
0:001> dt foo!MyClass
   +0x000 IntMemberVariable : Int4B
   +0x004 FloatMemberVariable : Float
   +0x008 BoolMemberVariable : Bool
   +0x00c PtrMemberVariable : Ptr32 MyClass
```

**Working With Templates**

You can use wild cards with the x command to display template classes as shown in this sample.

```dbgcmd
0:001>  x Fabric!Common::ConfigEntry*TimeSpan?
000007f6`466a2f9c Fabric!Common::ConfigEntry<Common::TimeSpan>::ConfigEntry<Common::TimeSpan> (void)
000007f6`466a3020 Fabric!Common::ConfigEntry<Common::TimeSpan>::~ConfigEntry<Common::TimeSpan> (void)
```

Consider using the [**dt (Display Type)**](dt--display-type-.md) command when working with templates, as the x command does not display individual template class items.

```dbgcmd
0:001> dt foo!Common::ConfigEntry<Common::TimeSpan>
   +0x000 __VFN_table : Ptr64 
   +0x008 componentConfig_ : Ptr64 Common::ComponentConfig
   +0x010 section_         : std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t> >
   +0x038 key_             : std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t> >
```

## <span id="see_also"></span>See also


[Verifying Symbols](verifying-symbols.md)

[**dv (Display Local Variables)**](dv--display-local-variables-.md)

 

 






