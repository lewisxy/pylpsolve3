from lpsolve55 import *

def lp_maker(f = None, a = None, b = None, e = None, vlb = None, vub = None, xint = None, scalemode = None, setminim = None):
  """LP_MAKER  Makes mixed integer linear programming problems.

  SYNOPSIS: lp_handle = lp_maker(f,a,b,e,vlb,vub,xint,scalemode,setminim)
     make the MILP problem
       max v = f'*x
         a*x <> b
           vlb <= x <= vub
           x(int) are integer

  ARGUMENTS: The first four arguments are required:
           f: n vector of coefficients for a linear objective function.
           a: m by n matrix representing linear constraints.
           b: m vector of right sides for the inequality constraints.
           e: m vector that determines the sense of the inequalities:
                     e(i) < 0  ==> Less Than
                     e(i) = 0  ==> Equals
                     e(i) > 0  ==> Greater Than
         vlb: n vector of non-negative lower bounds. If empty or omitted,
              then the lower bounds are set to zero.
         vub: n vector of upper bounds. May be omitted or empty.
        xint: vector of integer variables. May be omitted or empty.
   scalemode: Autoscale flag. Off when 0 or omitted.
    setminim: Set maximum lp when this flag equals 0 or omitted.

  OUTPUT: lp_handle is an integer handle to the lp created."""

  if f == None:
          help(lp_maker)
          return

  m = len(a)
  n = len(a[0])
  lp = lpsolve(b'make_lp', m, n)
  lpsolve(b'set_verbose', lp, IMPORTANT)
  lpsolve(b'set_mat', lp, a)
  lpsolve(b'set_rh_vec', lp, b)
  lpsolve(b'set_obj_fn', lp, f)
  lpsolve(b'set_maxim', lp) # default is solving minimum lp.

  for i in range(m):
    if e[i] < 0:
          con_type = LE
    elif e[i] == 0:
          con_type = EQ
    else:
          con_type = GE
    lpsolve(b'set_constr_type', lp, i + 1, con_type)

  if vlb != None:
    for i in range(n):
      lpsolve(b'set_lowbo', lp, i + 1, vlb[i])

  if vub != None:
    for i in range(n):
      lpsolve(b'set_upbo', lp, i + 1, vub[i])

  if xint != None:
    for i in range(len(xint)):
      lpsolve(b'set_int', lp, xint[i], 1)

  if scalemode != None:
    if scalemode != 0:
      lpsolve(b'set_scaling', lp, scalemode)

  if setminim != None:
    if setminim != 0:
      lpsolve(b'set_minim', lp)
    else:
      lpsolve(b'set_maxim', lp);

  return lp
