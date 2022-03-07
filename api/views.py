from report.models import Report
from django.views import View
from django.http.response import JsonResponse
from report.models import Report
from django.forms.models import model_to_dict
import logging 

logger = logging.getLogger(__name__)

class ReportAPI(View):

    def get(self, request, id=None, conversation_id=None):
        response = None

        if id != None:
            try:
                report = Report.objects.get(id=id)
                response = {
                    "status_code": 0,
                    "address_text": report.address_text,
                    "address_value": report.address_value,
                    "conversation_id": report.conversation_id,
                    "customer_phone": report.customer_phone,
                }
            except Exception as e:
                logger.debug(f"ReportAPI - ID: {id} has an error: {e}")
                response = {
                    "status_code": 0,
                    "error": str(e)
                }
            finally:
                return JsonResponse(response,safe=False, json_dumps_params={'ensure_ascii': False})
                
        if conversation_id != None:
            response = None
            try:
                report = Report.objects.get(conversation_id=conversation_id)
                response = {
                    "status_code": 0,
                    "address_text": report.address_text,
                    "address_value": report.address_value,
                    "conversation_id": report.conversation_id,
                    "customer_phone": report.customer_phone,
                }
            except Exception as e:
                logger.debug(f"ReportAPI - ConversationID: {conversation_id} has an error: {e}")
                response = {
                    "status_code": 1,
                    "error": str(e)
                }
            finally:
                return JsonResponse(response,safe=False, json_dumps_params={'ensure_ascii': False})
        
        try:
            reports = Report.objects.all()
            reports = [model_to_dict(report) for report in reports]
            response = {
                "status_code": 0,
                "reports": reports
            }
        except Exception as e:
            logger.debug(f"ReportAPI - GET ALL REPORTS has an error: {e}")
            response = {
                "status_code": 1,
                "error": str(e)
            }
        finally:
            return JsonResponse(response,safe=False, json_dumps_params={'ensure_ascii': False})
            
    
    def post(self, request):
        response = None
        try:
            conversation_id = request.POST['conversation_id']
            address_value = request.POST['address_value']
            address_text = request.POST["address_text"]
            location = eval(request.POST["location"])
            customer_phone = request.POST["customer_phone"]
            print("location: ", location)
            report = Report(conversation_id=conversation_id, address_text=address_text, address_value=address_value, location=location, customer_phone=customer_phone)
            report.save()
            response = {
                "status_code": 0,
                "msg": "create a report successfully !"
            }
        except Exception as e:
            logger.debug(f"ReportAPI - CREATE A REPORT has an error: {e}")
            response = {
                "status_code": 1,
                "error": str(e)
            }
        finally:
            return JsonResponse(response,safe=False, json_dumps_params={'ensure_ascii': False})


