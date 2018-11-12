---
title: Selection
description: Selection
ms.assetid: 5DFE5B52-4D58-491c-9363-95E4A2FD680C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selection


Test Authoring and Execution Framework (TAEF) provides a mechanism to selectively run or omit certain tests based on the metadata information you provide. The following section goes through various examples of how to use this selection mechanism with TE.exe.

You can run TE.exe from a command prompt window.

``` syntax
TE <test_binaries> [/select:<selection criteria>]
```

This section describes the TE.exe **/select:**<em>selection criteria</em> option. For more information about TE.exe, see [TE.exe Command Options](te-exe-command-line-parameters.md).

The selection criteria gets applied globally to all the test binaries that have been mentioned at the command prompt. Let's consider two test\_binaries: **Examples\\CPP.SelectionCriteria1.Example.dll** and **Examples\\CPP.SelectionCriteria2.Example.dll** . The following example shows the properties, or metadata, specifed at the various levels in these test\_binaries. You can also obtain this by specifying the **/listproperties** option in the Command Prompt window.

```cpp
CPP.SelectionCriteria1.Example.dll (Owner="C1", Priority=3)
class11 (Owner="C2")
method111(Priority=1)

method112 (BackwardsCompatibility="Windows 2000")
class12
method121
CPP.SelectionCriteria2.Example.dll (Owner="WEX")
class21 (Owner="C1", Priority=2, BackwardsCompatibility="Windows XP")
method211 (Owner="C2")
class22 (Owner="U3")
method221
```

In other words, by using /listproperties on each one of these test\_binaries separately, you get:

``` syntax
F:\fsd1.binaries.x86chk\WexTest\C1\TestExecution>te Examples\CPP.SelectionCriteria1.Example.dll /listproperties
Test Authoring and Execution Framework v2.2 Build 6.1.7689.0 (release.091218-1251) for x86

F:\fsd1.binaries.x86chk\WexTest\C1\TestExecution\Examples\CPP.SelectionCriteria1.Example.dll
        Property[Owner] = C1
        Property[Priority] = 3
    WEX::TestExecution::Examples::Class11
            Property[Owner] = C2
        WEX::TestExecution::Examples::Class11::Method111
                Property[Priority] = 1
        WEX::TestExecution::Examples::Class11::Method112
                Property[BackwardsCompatibility] = Windows2000

    WEX::TestExecution::Examples::Class12
        WEX::TestExecution::Examples::Class12::Method121
```

And:

``` syntax
F:\fsd1.binaries.x86chk\WexTest\C1\TestExecution>te Examples\CPP.SelectionCriteria2.Example.dll /listproperties
Test Authoring and Execution Framework v2.2 Build 6.1.7689.0 (release.091218-1251) for x86

F:\fsd1.binaries.x86chk\WexTest\C1\TestExecution\Examples\CPP.SelectionCriteria2.Example.dll
        Property[Owner] = WEX
    WEX::TestExecution::Examples::Class21
            Property[BackwardsCompatibility] = Windows XP
            Property[Owner] = C1
            Property[Priority] = 2
        WEX::TestExecution::Examples::Class21::Method211
                Property[Owner] = C2

    WEX::TestExecution::Examples::Class22
            Property[Owner] = U3
        WEX::TestExecution::Examples::Class22::Method221
```

It is important to note at this point that test\_binaries are listed along with their full path, and class names are listed as "&lt;Namespace&gt;::&lt;ClassName&gt;" in the case of native test\_binaries and "&lt;Namespace&gt;.&lt;ClassName&gt;" in the case of managed test\_binaries. Similarly, test method names are listed as "&lt;Namespace&gt;::&lt;ClassName&gt;::&lt;TestMethodName&gt;" in the case of native test\_binaries and "&lt;Namespace&gt;.&lt;ClassName&gt;.&lt;TestMethodName&gt;" in the case of managed test\_binaries.

In other words, the fully qualified name of any name or function is what is saved in te. This is to allow the ability to uniquely distinguish any method. For example if two classes have the same method name, the class qualification helps to uniquely select the method you are interested it. Toward this end, selection criteria helps to run only those tests that match your criteria in the given test\_binaries.

In the above example, say in Examples\\Cpp.SelectionCriteria1.Example.dll, you can choose "Method111" by any of the following selection criteria:

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll /select:"@Name='WEX::TestExecution::Examples::Class11::Method111'"
```

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll /select:"@Name='*Class11::Method111'"
```

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll /select:"@Name='*Method111'"
```

You can choose to run all tests that have been marked up with "Priority" less than 2 by running:

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll /select:"@Priority < 2"
```

This would run only Examples\\CPP.SelectionCriteria1.Example.dll - "class11::method111" in our example.

If you want to run all tests under class11, you could use the qualified "Name" property along with wildcard matching to choose it as follows:

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll
                                                               /select:"@Name='*::class11::*'"
```

When using selection criteria, there are some things useful to keep in mind:

-   "**and**", "**not**", and "**or**" are **reserved** words and are **case insensitive**.
-   **metadata property names and values are case insensitive**, for example "C2" in the example, would match "c2" and "C2". Hence if you have one function with metadata "property" and another with "Property" and the selection criteria is looking for "PROPERTY", it would match both of these.
-   **String value in the selection query string should be included in single quotes. Within a string value in selection query "?" is a single wildcard character and "\*" is 0 or more wildcard characters.**
-   While using quotes at your command prompt, **be mindful of smart quotes when you copy over a selection query**. If you copy over a selection query from an Outlook e-mail, you may accidentally have smart quotes, and TAEF may be unable to parse it. Type out the quotes instead.

Let's go over some quick examples of compound selection criteria and what they would execute.

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"@Owner='C2' AND @Priority=2"
```

Will run:

-   Examples\\CPP.SelectionCriteria2.Example.dll - class21::method211

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"@Owner='C2' AND @Priority=3"
```

Will run:

-   Examples\\CPP.SelectionCriteria1.Example.dll - class11::method112

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"@Owner='U3' oR @Priority=1"
```

Will run:

-   Examples\\CPP.SelectionCriteria1.Example.dll - class11::method111
-   Examples\\CPP.SelectionCriteria2.Example.dll - class22::method221

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"not(@BackwardsCompatibility=*)"
```

Will run all tests where BackwardsCompatibility value has not been specified. (See the following items.)

-   Examples\\CPP.SelectionCriteria1.Example.dll - class11::method111, class12::method121
-   Examples\\CPP.SelectionCriteria2.Example.dll - class22::method221

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"@Owner='C*'"
```

will run all tests where Owner value starts with "C" (case insensitive). Thus, the previous command will run all tests in Examples\\CPP.SelectionCriteria1.Example.dll and all tests in Examples\\CPP.SelectionCriteria2.Example.dll under class21 (that is, method211)

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"not(@BackwardsCompatibility=*) OR (@Owner='C*' AND @BackwardsCompatibility='*XP*')"
```

will run all tests where either the BackwardsCompatibility is not specified or, where the owner name begins with "C" and backwardsCompatibilty value contains XP. NOTE how the parenthesis "(" and ")" are used to specify the precedence order.

In the example, this would selectively run:

-   Examples\\CPP.SelectionCriteria1.Example.dll - class11::method111, class12::method121,
-   Examples\\CPP.SelectionCriteria2.Example.dll - class21::method211, class22::method221

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll /select:"@Owner='???'"
```

will only run tests that have property owner value containing only 3 characters.

In our example, this would match "C" and run only:

-   Examples\\CPP.SelectionCriteria1.Example.dll - class12::method121

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll /select:"@Priority>=1"
```

NOTE: This is good example of how you can use "&gt;=", "&lt;=", "&gt;" and "&lt;" where propertyvalues are floatvalues.

In our example this would run all methods except Examples\\CPP.SelectionCriteria2.Example.dll - class22::method221, where no prority has been specified. In other words, this would run:

-   Examples\\CPP.SelectionCriteria1.Example.dll - class11::method111, class11::method112, class12::method121
-   Examples\\CPP.SelectionCriteria2.Example.dll - class21::method211.

NOTE that you can use "/select" in conjuction with other command options like "/list" "/listproperties" etc.

## <span id="Smart_Quotes"></span><span id="smart_quotes"></span><span id="SMART_QUOTES"></span>Smart Quotes


You may encounter smart quotes in your selection criteria if you are copying over a selection criteria from Outlook or Word document back over to your command prompt. You can find more information about what smart quotes are on: <http://en.wikipedia.org/wiki/Smart_quotes> and [Smart quotes: The hidden scourge of text meant for computer consumption](https://blogs.msdn.microsoft.com/oldnewthing/20090225-00/?p=19033/)

There is no easy way to avoid smart quotes - best approach is to delete all of the " double quotes and ' single quotes in the selection criteria after you have copied it over to the command prompt and retype the quotes part of the query.

There is an options setting to turn them off when creating messages in Outlook. Type "smart quotes" into the Outlook help box to find this.

## <span id="Quick_Name_based_selection"></span><span id="quick_name_based_selection"></span><span id="QUICK_NAME_BASED_SELECTION"></span>Quick Name based selection


TAEF allows a quick selection based on name at the command prompt using the '/name' command line parameter:

``` syntax
/name:<test name with wildcards>
```

is equivalent to:

``` syntax
/select:@Name='<test name with wildcards>'
```

In other words, you can now provide a selection query based on name like:

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll \
/select:"@Name='*::class11::*'"
```

more quickly by using **/name** like so:

``` syntax
Te.exe Examples\CPP.SelectionCriteria1.Example.dll Examples\CPP.SelectionCriteria2.Example.dll /name=*::class11::*
```

Note that if both **/name** and **/select** are provided at the command prompt, then /name is ignored and /select takes precedence.

 

 





