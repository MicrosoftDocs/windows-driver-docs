---
title: Executing Data-driven tests
description: Executing Data-driven tests
ms.assetid: E8E7A66A-6E39-442d-A195-AE4633B817FE
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="taef.executing_data-driven_tests"></span>Executing Data-driven tests


Make sure you are aware of how to author Data-driven tests and how to execute tests with [TAEF](index.md) before you start with tips and tricks of executing DataDrivenTests with TAEF. It might be helpful to refresh your memory on how [selection query](selection.md) works with TAEF as well.

This section specifically talks about executing table based data-driven tests, but the same basic principle apply to PICT based and WMI based data-driven tests as well.

If you just want to run all your tests, including data driven tests, there is no difference from how you would normally run it with TAEF. Let's consider an example of running our **CPP\\DataDrivenExample** and **CSharp\\DataDrivenExample** together using TAEF. Remember that by default TAEF runs tests out-of-proc. If you want to run them inproc, use the "/inproc" switch.

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll Examples\CSharp.DataDriven.Example.dll
```

Take a look at the xml files and header files that specify the metadata. Run only the datadriven tests which have priority=1 as follows:

``` syntax
TE.exe Examples\*.Tests.dll /select:"@DataSource=* And @Priority=1"
```

Keep in mind that metadata specified at the row level in the xml file overrides the metadata specified at the TestMethod authoring level.

Let's explore a little more of the power of data driven test execution with TAEF. Say, you want to repro only the 3rd row in the FirstTable() function. You can do this by using the index of the row, which will be 2 (index starts at 0):

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll /select:"@Name='*FirstTable*' and @Data:index=2"
```

Notice that the selection criterion now has a new namespace "@Data:" which can be specifically used for data driven tests. When you run the above test, you will notice that instead of the usual '\#index' that gets appended to test names in case of data-driven tests, you have '\#Black' appended to the test name - this is the special 'Name' metadata specified for this row. See [Specifying metadata at the Row level](metadata-overriding-data-driven-test-example.md) for details. Despite this special name, you can still select using the name. The index selection can go a long way to select a range of rows for a really large data set. For example (hypothetical - not in example) if you have a data driven tests with 100 rows (max index = 99) and you only want to execute rows with index greater than 10 and less than 20, you can now easily specify this as:

``` syntax
TE.exe Examples\*.Tests.dll /select:"@Name='*MyDataDrivenTest*' and @Data:index > 10 and @Data:index < 20"
```

Many a times, you would want to repro based on a particular data value and not have to go through the trouble of finding its index. In this case you can use the "@Data:" namespace again. Now say in the native example of unit tests (see [Authoring data-driven tests](data-driven-testing.md)), you want to run only those cases when "Theme" is "AeroBasic".

``` syntax
TE.exe Examples\CPP.DataDriven.Example.dll Examples\CSharp.DataDriven.Example.dll /select:"@Data:Theme='AeroBasic'"
```

This will show on the console as follows:

``` syntax
StartGroup: WEX::TestExecution::Examples::DataDrivenTests::SecondTable#2 [Process: 3588; Thread: 4584]
I am in second table.
Theme supplied as AeroBasic
EndGroup: WEX::TestExecution::Examples::DataDrivenTests::SecondTable#2 [Passed]
Summary: Total=1, Passed=1, Failed=0, Blocked=0, Not Run=0, Skipped=0
```

You can also leverage /listproperties for datadriven tests to see the data sets and the metadata (combination of metadata specified at the test method level and row level) for the data driven test. So,

``` syntax
TE.exe Examples\CSharp.DataDriven.Examples.dll /listproperties
```

will list all the methods (datadriven and otherwise) along with the metadata and data values available and specified at various levels.

Take a look at [Overriding metadata at the Row level](metadata-overriding-data-driven-test-example.md), [Specifying array parameter types](array-support-data-driven-test-example.md) and [Simple data-driven example](data-driven-testing.md) for example walk-throughs providing more insight.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Executing%20Data-driven%20tests%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




