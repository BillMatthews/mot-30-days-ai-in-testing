val = ('',
 [
     ('What are the steps require in Active Learning?', "Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\nYou can learn passively by watching a lecture or reading a book. This constitutes\nsome learning and will compound very slowly. You can take notes while\nwatching a lecture. Now we are starting to get somewhere. You can review your\nnotes the next day. You move even faster.\nIf you add some exercises to the mix, your speed increases even more. If your\nexercises morph into mini-projects that you share with the world, you are\nmoving very fast.\nThe more atoms you move the better the feedback you receive and the greater\nthe extent to which you can reflect on what you are learning.\n36 Do genuine work (it compounds)\n\nthat in the lecture, it is time to go a step further. This time, we search for a\nsimilar dataset and test drive the technique we just learned about. Your\nimagination is the only limit here. You could seek out a dataset online or you\ncould put one together yourself. [4]\n Alternatively, the fast.ai library provides\naccess to many datasets  used for research. You can download them to your\nmachine with a single command.\nThe idea is to systematically grow your skills. You start in a controlled setting of\nthe lecture notebook, learning the ins and outs of the technique that the lecture\ndiscussed. With every new exercise, more of the training wheels come off, to the\npoint where you’re doing everything on your own from start to finish.\nThis approach to learning works like a charm. There are no hard and fast rules\nhere and you are more than welcome to modify it as you go. Being creative and\ncoming up with exercises that are challenging and interesting to you is a very\n\nunderstand how to optimize the training process itself. [20]\n. I would follow any of\nthese paths and learn the related theory in the process.\nTheory vs practice 19\n\nIt all begins with watching a lecture. The next step is to open the lecture\nnotebook and figure out how all the pieces fit together. The idea is to run each\n10 From not being able to program to deep learning expert\n\nQuestion: What are the steps require in Active Learning?\nHelpful Answer: Active learning is the process of using exercises to grow skills. The steps required for active learning are:\n1. Watch a lecture\n2. Create exercises based on the lecture\n3. Test drive the new technique learned in the lecture on a new dataset or a similar dataset\n4. Repeat this process systematically to grow skills over time.\nThe more challenging and interesting the exercises, the greater the extent to which skills are grown.")
 ]
 )

gen_out = val[1][0][1]
response_start_token="Helpful Answer:"
idx = gen_out.index(response_start_token)
print(idx)
#print(gen_out[:idx])
print(gen_out[idx:])