# //pub/std/imperial/dimensional-lumber

Dimensional lumber and plywood in imperial units, as parametric parts.

A piece of lumber is named by its **nominal** size ("2x4"): the size of the
rough-sawn board before it is dried and planed. What is sold is smaller, by the
amounts ALSC PS 20 gives -- a nominal 1 in. is 3/4 in. actual, 2 to 7 in. lose
1/2 in., and 8 in. and up lose 3/4 in. -- so a 2x4 is 1-1/2 x 3-1/2 in. The
length is not dressed: an 8 ft. board is 96 in. long. Plywood is named by its
nominal thickness and is 1/32 in. thinner than that.

The size parameters are the nominal sizes; the geometry is the actual one. Each
part also takes a `tolerance`: how precisely it is made, in millimetres -- 1.6
(1/16 in.) for lumber and 0.8 (1/32 in.) for plywood by default, which is what a
saw cuts either to and what a part cut from it has to be made to.

| Part      | Parameters                                                                  | Frame                                                   |
|-----------|-----------------------------------------------------------------------------|---------------------------------------------------------|
| `lumber`  | `width`, `height` (nominal, in.), `length` (in.), `tolerance` (mm)          | width along X, length along Y, height along Z; eased long edges |
| `plywood` | `width`, `length` (in.), `thickness` (nominal, in.), `tolerance` (mm)       | width along X, length along Y, thickness along Z        |

Both have a corner at the origin, so a piece cut to length from a longer board
is in the coordinates of the board it came from.

## Usage

```shell
pc inspect -p width=4 -p height=2 -p length=96 //pub/std/imperial/dimensional-lumber:lumber
```

From another package, as an instance of a standard size:

```yaml
parts:
  stud:
    type: enrich
    source: //pub/std/imperial/dimensional-lumber:lumber
    with:
      width: 4
      height: 2
      length: 92.625
```

## Products

A store advertises the sizes it sells by declaring each product as an instance
of `lumber` or `plywood` (an `enrich`) with its own `vendor` and `sku`. See
[`//pub/svc/commerce/homedepot`](https://github.com/partcad/svc-commerce-homedepot),
whose products the
[`//pub/furniture/workspace/basic`](https://github.com/partcad/partcad-furniture-basic)
desk is cut from.
