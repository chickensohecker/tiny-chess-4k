# tiny-chess-4k

A chess engine in at most 4,096 bytes of Python, written for the
[make.fun bounty "Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01).

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/chickensohecker/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/chickensohecker/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01)

## The engine

`main.py` is the whole engine: a 0x88 board, alpha-beta search with a
transposition table, killer moves, null-move pruning, late-move reductions
and a capture quiescence, over an incremental tapered piece-square
evaluation. It searches to a fixed node budget per move, never a clock,
so a trial's replay plays the same moves.

## Play

The engine talks to the trial env at `MAKEFUN_ENV_URL` only: `POST /game`
serves the game in play, `POST /move` plays a move in UCI, and it exits
when the env answers `done`. It makes no model calls.

## License

MIT, see LICENSE.
