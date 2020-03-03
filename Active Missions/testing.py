#!/usr/bin/env pybricks-micropython
import functions as toast
# Max Speed is 1050
# 25% is 262.5
# 50% is 525
# 75% is 787.5
medProcess = toast.Process(target=toast.med_attachment, args=(-45,))
medProcess.start()
toast.moveInches(20)
medProcess.join()





# Old robot testing:

# six inches at 25% was 1/16 off
# six inches at 25% was 3/32 off
# six inches at 25% was 1/16 off
# six inches at 25% was 1/32 off

# six inches at 50% was 3/32 off
# six inches at 50% was 1/32 off
# six inches at 50% was 1/16 off
# six inches at 50% was 1/32 off

# six inches at 75% was 1/16 off
# six inches at 75% was 1/32 off
# six inches at 75% was 1/32 off
# six inches at 75% was -1/4 off: it curved one degree to the left

# six inches at 100% was 1/32 off
# six inches at 100% was 1/4 off
# six inches at 100% was 1/32 off
# six inches at 100% was 1/4 off

# twelve inches at 25% was 3/32 off
# twelve inches at 25% was -1/4 off
# twelve inches at 25% was -1/4 off
# twelve inches at 25% was -1/4 off

# twelve inches at 50% was -1/4 off
# twelve inches at 50% was -5/16 off
# twelve inches at 50% was -5/16 off
# twelve inches at 50% was -1/4 off

# twelve inches at 75% was -1/4 off
# twelve inches at 75% was -3/16 off
# twelve inches at 75% was -5/16 off
# twelve inches at 75% was -1/4 off

# twelve inches at 100% was -1/4 off
# twelve inches at 100% was -1/4 off
# twelve inches at 100% was -5/16 off
# twelve inches at 100% was -5/16 off


# Circ from 54 to 52

# six inches at 25% was 1/8 off
# six inches at 25% was 2/16 off

# changed to 53

# six inches at 25% was perfect
# six inches at 25% was perfect
# six inches at 25% was perfect

# twelve inches at 25% was perfect
# twelve inches at 75% was curved but pretty good.



