from flask import Flask, render_template, request, url_for
from time import gmtime, strftime

app = Flask("__name__")

@app.route('/', methods=['GET', 'POST'])
def index():
  qualified = 0
  msg = None
  # Get Ip --
  hit_ip = request.remote_addr
  timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  with open('IP_hits.txt', 'a') as the_file:
    the_file.write(str(hit_ip)+' : '+str(qualified)+'-- '+timestamp+'\n')
  if request.method == 'POST':
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    name = request.form['user_name']
    submit_ip = request.remote_addr
    with open('IP_hits.txt', 'a') as the_file:
      the_file.write(str(submit_ip)+' : '+str(qualified)+'-- '+str(name)+'-- '+timestamp+'\n')
    items = []
    #Row -- 0
    items.append(request.form['00'])
    items.append(request.form['02'])    
    items.append(request.form['04'])
    items.append(request.form['06'])
    items.append(request.form['07'])
    items.append(request.form['08'])
    #Row -- 1
    items.append(request.form['12'])
    items.append(request.form['13'])
    items.append(request.form['14'])
    items.append(request.form['17'])
    items.append(request.form['18'])
    #Row -- 2
    items.append(request.form['20'])
    items.append(request.form['21'])
    items.append(request.form['22'])
    items.append(request.form['23'])
    items.append(request.form['25'])
    items.append(request.form['26'])
    items.append(request.form['27'])
    items.append(request.form['28'])
    #Row -- 3
    items.append(request.form['32'])
    items.append(request.form['33'])
    items.append(request.form['34'])
    items.append(request.form['35'])
    items.append(request.form['37'])
    items.append(request.form['38'])
    #Row -- 4
    items.append(request.form['41'])
    items.append(request.form['42'])
    items.append(request.form['43'])
    items.append(request.form['44'])
    items.append(request.form['45'])
    items.append(request.form['46'])
    items.append(request.form['47'])
    #Row -- 5
    items.append(request.form['50'])
    items.append(request.form['51'])
    items.append(request.form['53'])
    items.append(request.form['54'])
    items.append(request.form['55'])
    items.append(request.form['56'])
    #Row -- 6
    items.append(request.form['60'])
    items.append(request.form['61'])
    items.append(request.form['62'])
    items.append(request.form['63'])
    items.append(request.form['65'])
    items.append(request.form['66'])
    items.append(request.form['67'])
    items.append(request.form['68'])
    #Row -- 7
    items.append(request.form['70'])
    items.append(request.form['71'])
    items.append(request.form['74'])
    items.append(request.form['75'])
    items.append(request.form['76'])
    #Row -- 8
    items.append(request.form['80'])
    items.append(request.form['81'])
    items.append(request.form['82'])
    items.append(request.form['84'])
    items.append(request.form['86'])
    items.append(request.form['88'])
  
    true_items = ['X','C','H','N','K','A','K','E','C','T','X','N','T','H','X','A','C','E','O','E','K','T','X','O','N','N','X','A','O','C','E','H','K','A','H','N','E','T','O','C','T','N','K','X','A','H','E','X','A','H','K','H','K','A','X','O','E']
    cap_item = []
    for i in items:
      cap_item.append(i.upper())
    print(cap_item)
    if cap_item == true_items:
      qualified = 1
      msg = 'Congratulations you won..!! :)'
      print("Matched")
      with open('IP_hits.txt', 'a') as the_file:
       the_file.write(str(submit_ip)+' : '+str(qualified)+'-- '+str(name)+'-- '+timestamp+'\n')
      return render_template('index.html', msg=msg)
    else:
      print("Not matching")
      msg = 'Sorry, Try again.. :('
      return render_template('index.html', msg=msg)

  return render_template('index.html')