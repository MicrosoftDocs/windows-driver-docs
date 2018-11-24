---
title: Authoring Tests in C++
description: Authoring Tests in C++
ms.assetid: ECADDDD6-5BD4-4c43-803F-47AE44467342
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authoring Tests in C++


The following code example shows a native C++ file that contains a single test class with two test methods on it.

```cpp
1   #include "WexTestClass.h"
2
3   class SimpleTests   {
4      // Declare this class as a TestClass, and supply metadata if necessary.
5      TEST_CLASS(SimpleTests);
6
7      // Declare the tests within this class.
8      TEST_METHOD(FirstTest);
9      TEST_METHOD(SecondTest);
10  };
11
12  void SimpleTests::FirstTest()
13  {
14      VERIFY_ARE_EQUAL(1, 1);
15  }
16
17  void SimpleTests::SecondTest()
18  {
19      VERIFY_IS_TRUE(true);
20  }
```

**Line 1** includes the single header file that is required for the framework, **WexTestClass.h**. That included header file also includes the **Log.h** file for the Logger and the **Verify.h** file for defining the verification cases. These header files will be discussed later.

**Line 3** defines a test Class, **SimpleTests**. Test classes do not need to inherit from any special class. Also, their contents do not need to be public.

**Line 5** defines this class as a test class.

**Lines 8 and 9** declare the two test methods in the class - **FirstTest** and **SecondTest**. They are defined on lines 12 through 20. The **TEST\_METHOD** macro adds the required method declaration to the class. In this mark-up scheme, all tests must have the same prototype. They must return **void**, and they must take no parameters.

If you wish to define the tests inline within the class declaration, you can do that as long as you include "WexTestClass.h" while **INLINE\_TEST\_METHOD\_MARKUP** is defined in the preprocessor.

```cpp
1   #define INLINE_TEST_METHOD_MARKUP
2   #include "WexTestClass.h"
3
4   class InlineTests
5   {
6       TEST_CLASS(InlineTests);
7 
8       TEST_METHOD(FirstTest)
9       {
10          VERIFY_ARE_EQUAL(1, 1);
11      }
12
13      TEST_METHOD(SecondTest)
14      {
15          VERIFY_IS_TRUE(true);
16      }
17  };
```

**Lines 10 and 15** now contain the definitions of the test methods.

**Note**  If you put your test class declaration in a header file, it is best to only include that header file into one cpp file. Including a test class declaration into multiple CPP files results in extratraneous data being compiled into the test DLL.

 

## <span id="Advanced_Authoring_Tests_in_C__"></span><span id="advanced_authoring_tests_in_c__"></span><span id="ADVANCED_AUTHORING_TESTS_IN_C__"></span>Advanced Authoring Tests in C++


The following example uses setup and cleanup methods and declares metadata along with the test class and test method declarations. This example also contains a single class (**MetadataAndFixturesTests**) with two test methods.

```cpp
 1  #define INLINE_TEST_METHOD_MARKUP
 2  #include "WexTestClass.h"
 3
 4  BEGIN_MODULE()
 5      MODULE_PROPERTY(L"Feature", L"TAEF")
 6  END_MODULE()
 7
 8  MODULE_SETUP(ModuleSetup)
 9  {
10      return true;
11  }
12
13  MODULE_CLEANUP(ModuleCleanup)
14  {
15      return true;
16  }
17
18  class MetadataAndFixturesTests
19  {
20      BEGIN_TEST_CLASS(MetadataAndFixturesTests)
21          TEST_CLASS_PROPERTY(L"Component", L"Verify")
22      END_TEST_CLASS()
23
24      TEST_CLASS_SETUP(ClassSetup)
25      {
26          return true;
27      }
28
29      TEST_CLASS_CLEANUP(ClassCleanup)
30      {
31          return true;
32      }
33
34      TEST_METHOD_SETUP(TestSetup)
35      {
36          return true;
37      }
38
39      TEST_METHOD_CLEANUP(TestCleanup)
40      {
41          return true;
42      }
43
44      // If you use this syntax, you will have to define the test outside of the test class.
45      BEGIN_TEST_METHOD(FirstTest)
46          TEST_METHOD_PROPERTY(L"Owner", L"Contoso")
47      END_TEST_METHOD()
48
49      // You can still have metadata even if you define your test inside the test class.
50      TEST_METHOD(SecondTest)
51      {
52          BEGIN_TEST_METHOD_PROPERTIES()
53              TEST_METHOD_PROPERTY(L"Owner", L"Contoso")
54          END_TEST_METHOD_PROPERTIES()
55
56          VERIFY_IS_TRUE(true);
57      }
58  };
59
60  void MetadataAndFixturesTests::FirstTest()
61  {
62      VERIFY_ARE_EQUAL(1, 1);
63  }
```

**Line 4** begins the declaration of global metadata, a set of properties that apply to a test binary for which this header compiles.

**Line 5** declares a property with the name **Feature** and the value **TAEF**. There could be more than a single property between BEGIN... and END... macros. Similar property declarations exist on lines 20-24 (class level metadata), 45-47 (method level metadata), and 52-54 (test level metadata in a test defined inline).

**Lines 45 - 47 and 60 – 63** demonstrate these test macros for adding metadata also declare the test methods. **Lines 50 - 57** demonstrate you can still have metadata even if you want to declare and define you test in the same location.

**Line 8** declares a module setup function - a function that executes before the creation of any of the module’s test classes.

**Line 13** declares a module cleanup function - a function that executes after all the test and the class cleanup methods and destructors finish. There are similar setup and cleanup methods for a class on lines 24 though 32. These methods run after the class constructor and before the class destructor respectively.

**Lines 34 through 42** declare similar functions for the test methods. Test setup and cleanup methods run before and after each test executes.

TAEF setup and cleanup methods return bool and accept no parameters. The return value signals to the framework whether it can continue to run tests for a certain test unit. For example, if a class setup method fails and returns false, the framework will not run the class test methods.

 

 





