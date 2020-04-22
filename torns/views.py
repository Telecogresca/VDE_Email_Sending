import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Torn
# Create your views here.

@permission_required('admin.can_add_log_entry')
def torns_upload(request):
	template = "torns_upload.html"

	prompt = {
		'order': 'Order of the CSV should be mote, name, last_name, email, phone'
	}

	if request.method == 'GET':
		return render(request, template, prompt)

	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')

	io_string = io.StringIO(data_set)
	#skip header
	next(io_string)
	for column in csv.reader(io_string, delimiter=','):
		    _, created = Torn.objects.update_or_create(
		    	date=column[0],
		    	day_of_week=column[1], 
		    	num_day=column[2], 
		    	start_h=column[3], 
		    	finish_h=column[4],
		    	kapo1=column[5], 
		    	kapo2=column[6], 
		    	email1=column[7],
		    	email2=column[8],
		    )
	context = {}
	return render(request, template, context)


	