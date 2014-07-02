HaskellBooster
==============

HaskellBooster is a set of tools and extensions improving Haskell's programmer workflow. HaskellBooster contains GHC extensions implemented as GHC preprocessors and simple command line tools wrappers (ghc, runhaskell, cabal), automatically providing needed flags when necessary.

###Extensions
All extensions are implemented as GHC preprocessors and can be enabled by defining pragmas using a little different syntax than standard Haskell's pragmas. HaskellBooster pragmas look like ordinary pragmas with exclamation mark on the beginning of the line. So aan example pragma would be ```!{-# LANGUAGE RightSideContexts #-}```.

####RightSideContexts
The pragma extends available syntax when defining type classes and type class instances. It allows writing the context on the right side of such declaration, after a new operator ```<=```. An example Haskell code
```haskell
instance (a1~a2, out~b)                                      => Pipe (a1 -> b)           a2             out where ...
instance (a1~a2, Monad m, Monad mx, out~(m b :> mx))         => Pipe (a1 -> b)           (m a2 :> mx)   out where ...
instance (a1~a2, mx1~Pure, Monad m1, out~b)                  => Pipe (m1 a1 :> mx1 -> b) a2             out where ...
instance (a1~a2, m1~m2, mx1~mx2, Monad m1, Monad mx1, out~b) => Pipe (m1 a1 :> mx1 -> b) (m2 a2 :> mx2) out where ...
instance (a1~a2, Monad m, Monad mx, out~(m b :> mx))         => Pipe (m (a1 -> b) :> mx) a2             out where ...
instance (a1~a2, Monad m, Monad mx, out~(m b :> mx))         => Pipe (m (a1 -> b) :> mx) (m a2 :> mx)   out where ...
```
becomes
```
instance Pipe (a1 -> b)           a2             out <= (a1~a2, out~b)                                      where ...
instance Pipe (a1 -> b)           (m a2 :> mx)   out <= (a1~a2, Monad m, Monad mx, out~(m b :> mx))         where ...
instance Pipe (m1 a1 :> mx1 -> b) a2             out <= (a1~a2, mx1~Pure, Monad m1, out~b)                  where ...
instance Pipe (m1 a1 :> mx1 -> b) (m2 a2 :> mx2) out <= (a1~a2, m1~m2, mx1~mx2, Monad m1, Monad mx1, out~b) where ...
instance Pipe (m (a1 -> b) :> mx) a2             out <= (a1~a2, Monad m, Monad mx, out~(m b :> mx))         where ...
instance Pipe (m (a1 -> b) :> mx) (m a2 :> mx)   out <= (a1~a2, Monad m, Monad mx, out~(m b :> mx))         where ...
```

####FixedComments
The extensions narrows lexical rules in the file it was used in such way, that ```--``` is always beginning of the one line comment. In standard Haskell syntax we need to keep in mind, that some characters after the comment symbol can cause to treat such comment as an operator.
For example former code is illegal in Haskell (because ```--|``` is interpreted as an operator), whenever it is legal with the extension
```haskell
data UnsafeBase base err val = Value val
                             --| Error err
                             | Other (base val)
                             deriving Show
```

####MultiLineStrings
This extensions allows using new multiline string type literal in Haskell. Multiline strings are defined between triple quotation marks and can be used as follow
```haskell
test = """ this is a proper
multiline string,
enabled with MultiLineStrings extension"""

main = putStrLn test
```

####Python
The extension allow injecting Python scripts inside Haskell source files. Python expressions can be written between tripple backquotes in any place in the code. Provided example code sets the value of variable ```rand``` to a random value for each compilation of the file
```haskell
 ```from random import random```
 rand = ```random()```
 main = print rand
```


###How to start
To start using HaskellBooster add the ```shell``` folder to your UNIX PATH environment variable. The wrappers for ```ghc```, ```runhaskell``` and ```cabal``` are provided there. To use HaskellBooster just replace all standard commands with commands containing exclamation mark at the end, for example ```ghc!``` or ```runhaskell!``` instead of ```ghc``` or ```runhaskell```
