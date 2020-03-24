# みんなの Java OpenJDK から始まる大変革期！

## JIT vs AOT, JVM vs Native(standalone executable file)

5-4 GraalVM の組み込みとネイティブイメージ

GraalVM Native Image 機能により Java でも standalone executable ファイルを生成できる。

起動時間やメモリディスク使用量は AOT の方が有利。

ただ，ピーク時のスループットや最大レイテンシは JIT の方が有利。  
これは，JIT の方がより実行時に最適な機械語を生成できるからということらしい。

https://www.infoq.com/jp/articles/Graal-Java-JIT-Compiler/

> JVM を起動すると、実行しているプロセッサが精査される。これにより JVM はその CPU で利用可能な機能を正確に把握できるようになる。使用中のプロセッサ特有の組み込み関数テーブルを構築する。JVM はハードウェアの能力を十分に活用できるということだ。
> これは AOT コンパイルと異なる。AOT コンパイルは一般的なチップ向けにコンパイルし、利用できる機能について仮説を慎重に立てなければならない。AOT コンパイルされたライブラリは実行時に現在の CPU でサポートされていない命令を実行しようとするとクラッシュするからだ。

他にも例えば以下の記載あるけど理解できていない。  
後で気が向いたら確認する。  
https://en.wikipedia.org/wiki/Just-in-time_compilation

> 2.The system is able to collect statistics about how the program is actually running in the environment it is in, and it can rearrange and recompile for optimum performance. However, some static compilers can also take profile information as input.  
> 3.The system can do global code optimizations (e.g. inlining of library functions) without losing the advantages of dynamic linking and without the overheads inherent to static compilers and linkers. Specifically, when doing global inline substitutions, a static compilation process may need run-time checks and ensure that a virtual call would occur if the actual class of the object overrides the inlined method, and boundary condition checks on array accesses may need to be processed within loops. With just-in-time compilation in many cases this processing can be moved out of loops, often giving large increases of speed.  
> 4.Although this is possible with statically compiled garbage collected languages, a bytecode system can more easily rearrange executed code for better cache utilization.

未確認。  
inside java - JIT コンパイラの実際の動作
https://www.oracle.com/webfolder/technetwork/jp/javamagazine/Java-MA16-JIT.pdf
