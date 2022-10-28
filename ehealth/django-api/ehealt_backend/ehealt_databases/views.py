from django.shortcuts import render

from django.views.generic import View

from .models import Person, Patient, Doctor, DoctorAcount, VitalSigns

from .models import PatientDiagnostic, PhoneNumbers, UserAccount

from django.http import JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt

import json


class person_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, person_id=0):

        if (person_id > 0):

            persons = list(Person.objects.filter(person_id=person_id).values())

            if len(persons) > 0:

                person = persons[0]

                data = {'person': person}

            else:

                data = {'msg': 'No person found'}

            return JsonResponse(data)

        else:

            persons = list(Person.objects.values())

            if len(persons) > 0:

                data = {'persons_list': persons}

            else:

                data = {'message': 'No persons registered yet'}

            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)

        Person.objects.create(person_id=jd['person_id'], name=jd['name'], second_name=jd['second_name'], lastname=jd['lastname'],
                              second_lastname=jd['second_lastname'], age=jd['age'])

        data = {'person_created': jd}

        return JsonResponse(jd)

    def put(self, request, person_id):

        jd = json.loads(request.body)

        persons = list(Person.objects.filter(person_id=person_id).values())

        if len(persons) > 0:

            person = Person.objects.get(person_id=person_id)

            person.name = jd['name']

            person.second_name = jd['second_name']

            person.lastname = jd['lastname']

            person.second_lastname = jd['second_lastname']

            person.age = jd['age']

            person.save()

            data = {'msg': jd}

        else:

            data = {'msg': 'Person with that id not registered'}

        return JsonResponse(data)

    def delete(self, request, person_id):

        persons = list(Person.objects.filter(person_id=person_id).values())

        if len(persons) > 0:

            Person.objects.filter(person_id=person_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'Nothing to delete'}

        return JsonResponse(data)


class patient_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, patient_id=0):

        if (patient_id > 0):

            persons = list(Person.objects.filter(
                person_id=patient_id).values())

            if len(persons) > 0:

                person = persons[0]

                data = {'person': person}

            else:

                data = {'msg': 'not found'}

            return JsonResponse(data)

        else:

            #persons = list(Patient.objects.values())
            persons = []
            elist = []
            patients = list(Patient.objects.all().values_list(
                'patient_id', flat=True))
            i = 0
            while i < len(patients):
                persons = list(Person.objects.filter(
                    person_id=patients[i]).values())
                elist.append(persons[0])
                i += 1

            if len(persons) > 0:

                data = {'persons': elist}

            else:

                data = {'message': 'not patients registered'}

            return JsonResponse(data)

    def post(self, request):

        #TipoCliente.objects.get(codigo = request.POST['tipo_cliente'])

        jd = json.loads(request.body)

        Person.objects.create(person_id=jd['person_id'], name=jd['name'], second_name=jd['second_name'], lastname=jd['lastname'],
                              second_lastname=jd['second_lastname'], age=jd['age'])

        Patient.objects.create(patient_id=jd['person_id'], person=Person.objects.get(
            person_id=jd['person_id']))

        UserAccount.objects.create(user_account_id=jd['person_id'],
                                   patient=Patient.objects.get(
                                       patient_id=jd['person_id']),
                                   username=jd['username'],
                                   user_email=jd['email'],
                                   user_password=jd['password'])

        data = {'return JsonResponse(data)': 'inserted patient'}

        return JsonResponse(data)

    def put(self, request, patient_id):

        jd = json.loads(request.body)

        persons = list(Person.objects.filter(person_id=patient_id).values())

        if len(persons) > 0:

            person = Person.objects.get(person_id=patient_id)

            person.name = jd['name']

            person.second_name = jd['second_name']

            person.lastname = jd['lastname']

            person.second_lastname = jd['second_lastname']

            person.age = jd['age']

            person.save()

            data = {'msg': 'updated'}

        else:

            data = {'msg': 'not found'}

        return JsonResponse(data)

    def delete(self, request, patient_id):

        persons = list(Person.objects.filter(person_id=patient_id).values())

        if len(persons) > 0:

            Person.objects.filter(person_id=patient_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'not deleted'}

        return JsonResponse(data)


class doctor_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, doctor_id=0):

        if (doctor_id > 0):

            persons = list(Person.objects.filter(person_id=doctor_id).values())

            if len(persons) > 0:

                person = persons[0]

                data = {'doctor': person}

            else:

                data = {'msg': 'doctor not found'}

            return JsonResponse(data)

        else:

            persons = list(Doctor.objects.values())

            if len(persons) > 0:

                data = {'persons': persons}

            else:

                data = {'message': 'not doctors registered'}

            return JsonResponse(data)

    def post(self, request):

        #TipoCliente.objects.get(codigo = request.POST['tipo_cliente'])

        jd = json.loads(request.body)

        Person.objects.create(person_id=jd['person_id'], name=jd['name'], second_name=jd['second_name'], lastname=jd['lastname'],
                              second_lastname=jd['second_lastname'], age=jd['age'])

        Doctor.objects.create(doctor_id=jd['person_id'], person=Person.objects.get(person_id=jd['person_id']),
                              title=jd['title'])

        DoctorAcount.objects.create(doctor_account_id=jd['person_id'],
                                    doctor=Doctor.objects.get(
                                        doctor_id=jd['person_id']),
                                    doctor_username=jd['username'],
                                    doctor_email=jd['email'],
                                    doctor_password=jd['password'])

        data = {'return JsonResponse(data)': jd}

        return JsonResponse(data)

    def put(self, request, doctor_id):

        jd = json.loads(request.body)

        persons = list(Person.objects.filter(person_id=doctor_id).values())

        if len(persons) > 0:

            person = Person.objects.get(person_id=doctor_id)

            person.name = jd['name']

            person.second_name = jd['second_name']

            person.lastname = jd['lastname']

            person.second_lastname = jd['second_lastname']

            person.age = jd['age']

            person.save()

            data = {'msg': 'updated'}

        else:

            data = {'msg': 'not found'}

        return JsonResponse(data)

    def delete(self, request, doctor_id):

        persons = list(Person.objects.filter(person_id=doctor_id).values())

        if len(persons) > 0:

            Person.objects.filter(person_id=doctor_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'not deleted'}

        return JsonResponse(data)


class doctor_account_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, doctor_account_id=0):

        if (doctor_account_id > 0):

            persons = list(DoctorAcount.objects.filter(
                doctor_account_id=doctor_account_id).values())

            if len(persons) > 0:

                person = persons[0]

                data = {'doctor_account': person}

            else:

                data = {'msg': 'doctor account not found'}

            return JsonResponse(data)

        else:

            persons = list(DoctorAcount.objects.values())

            if len(persons) > 0:

                data = {'persons': persons}

            else:

                data = {'message': 'not doctors registered'}

            return JsonResponse(data)

    def post(self, request):
        #TipoCliente.objects.get(codigo = request.POST['tipo_cliente'])
        jd = json.loads(request.body)

        DoctorAcount.objects.create(doctor_account_id=jd['doctor_account_id'],
                                    doctor=Doctor.objects.get(
                                        doctor_id=jd['doctor_account_id']),
                                    doctor_username=jd['username'],
                                    doctor_email=jd['email'],
                                    doctor_password=jd['password'])

        data = {'return JsonResponse(data)': jd}

        return JsonResponse(data)

    def put(self, request, doctor_account_id):

        jd = json.loads(request.body)

        persons = list(DoctorAcount.objects.filter(
            doctor_account_id=doctor_account_id).values())

        if len(persons) > 0:

            person = DoctorAcount.objects.get(
                doctor_account_id=doctor_account_id)

            person.doctor_account_id = jd['doctor_account_id']

            person.doctor = Doctor.objects.get(
                doctor_id=jd['doctor_account_id'])

            person.doctor_username = jd['username']

            person.doctor_email = jd['email']

            person.doctor_password = jd['password']

            person.save()

            data = {'msg': 'updated'}

        else:

            data = {'msg': 'not found'}

        return JsonResponse(data)

    def delete(self, request, doctor_account_id):

        persons = list(DoctorAcount.objects.filter(
            doctor_account_id=doctor_account_id).values())

        if len(persons) > 0:

            DoctorAcount.objects.filter(
                doctor_account_id=doctor_account_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'not deleted'}

        return JsonResponse(data)


class user_account_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, user_account_id=0):

        if (user_account_id > 0):

            persons = list(UserAccount.objects.filter(
                user_account_id=user_account_id).values())

            if len(persons) > 0:

                person = persons[0]

                data = {'user_account': person}

            else:

                data = {'msg': 'user account not found'}

            return JsonResponse(data)

        else:

            persons = list(UserAccount.objects.values())

            if len(persons) > 0:

                data = {'users': persons}

            else:

                data = {'message': 'no users registered'}

            return JsonResponse(data)

    def post(self, request):
        #TipoCliente.objects.get(codigo = request.POST['tipo_cliente'])
        jd = json.loads(request.body)

        UserAccount.objects.create(user_account_id=jd['user_account_id'],
                                   patient=Patient.objects.get(
                                       patient_id=jd['user_account_id']),
                                   username=jd['username'],
                                   user_email=jd['email'],
                                   user_password=jd['password'])

        data = {'return JsonResponse(data)': jd}

        return JsonResponse(data)

    def put(self, request, user_account_id):

        jd = json.loads(request.body)

        persons = list(UserAccount.objects.filter(
            user_account_id=user_account_id).values())

        if len(persons) > 0:

            person = UserAccount.objects.get(user_account_id=user_account_id)

            person.user_account_id = jd['user_account_id']

            person.patient = Patient.objects.get(
                patient_id=jd['user_account_id'])

            person.user_username = jd['username']

            person.user_email = jd['email']

            person.user_password = jd['password']

            person.save()

            data = {'msg': 'updated'}

        else:

            data = {'msg': 'not found'}

        return JsonResponse(data)

    def delete(self, request, user_account_id):

        persons = list(UserAccount.objects.filter(
            user_account_id=user_account_id).values())

        if len(persons) > 0:

            UserAccount.objects.filter(
                user_account_id=user_account_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'not deleted'}

        return JsonResponse(data)


class user_phone_numbers_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, patient_id=0):

        if (patient_id > 0):

            persons = list(PhoneNumbers.objects.filter(
                patient=patient_id).values())

            if len(persons) > 0:

                data = {'user phones': persons}

            else:

                data = {'msg': 'user account not found'}

            return JsonResponse(data)

        else:

            persons = list(PhoneNumbers.objects.values())

            if len(persons) > 0:

                data = {'users': persons}

            else:

                data = {'message': 'no phones registered'}

            return JsonResponse(data)

    def post(self, request):
        #TipoCliente.objects.get(codigo = request.POST['tipo_cliente'])
        jd = json.loads(request.body)

        PhoneNumbers.objects.create(phone_number=jd['phone_number'],
                                    phone_content=jd['phone_content'],
                                    patient=Patient.objects.get(
                                        patient_id=jd['patient_id']),
                                    )

        data = {'return JsonResponse(data)': jd}

        return JsonResponse(data)

    def put(self, request, patient_id):

        jd = json.loads(request.body)

        persons = list(PhoneNumbers.objects.filter(
            patient=patient_id).values())

        if len(persons) > 0:

            person = PhoneNumbers.objects.get(patient=patient_id)

            person.phone_number = jd['phone_number']

            person.phone_content = jd['phone_content']

            person.patient = Patient.objects.get(patient_id=jd['patient_id'])

            person.save()

            data = {'msg': 'updated'}

        else:

            data = {'msg': 'not found'}

        return JsonResponse(data)

    def delete(self, request, patient_id):

        persons = list(PhoneNumbers.objects.filter(
            patient=patient_id).values())

        if len(persons) > 0:

            PhoneNumbers.objects.filter(patient=patient_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'not deleted'}

        return JsonResponse(data)


class diagnostic_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, patient=0):

        if (patient > 0):

            patients = list(PatientDiagnostic.objects.filter(
                patient=patient).values())

            if len(patients) > 0:

                diagnostics = []
                
                i=0

                while i < len(patients):            
                    diagnostics.append(patients[i])
                    i += 1

                data = {'diagnostic': diagnostics}

            else:

                data = {'msg': 'not found'}

            return JsonResponse(data)

        else:

            persons = list(PatientDiagnostic.objects.values())

            if len(persons) > 0:

                data = {'users': persons}

            else:

                data = {'message': 'nothing registered'}

            return JsonResponse(data)

    def post(self, request):
        #TipoCliente.objects.get(codigo = request.POST['tipo_cliente'])
        jd = json.loads(request.body)

        PatientDiagnostic.objects.create(
            diagnostic_text=jd['diagnostic_text'],
            patient=Patient.objects.get(patient_id=jd['patient_id']),
            doctor=Doctor.objects.get(doctor_id=jd['doctor_id'])
        )

        data = {'diagnostico': jd}

        return JsonResponse(data)

    def put(self, request, diagnostic_id):

        jd = json.loads(request.body)

        persons = list(PatientDiagnostic.objects.filter(
            diagnostic_id=diagnostic_id).values())

        if len(persons) > 0:

            person = PatientDiagnostic.objects.get(diagnostic_id=diagnostic_id)

            person.diagnostic_id = jd['diagnostic_id']

            person.diagnostic_text = jd['diagnostic_text']

            person.patient = Patient.objects.get(patient_id=jd['patient_id'])

            person.doctor = Doctor.objects.get(doctor_id=jd['doctor_id'])

            person.save()

            data = {'msg': 'updated'}

        else:

            data = {'msg': 'not found'}

        return JsonResponse(data)

    def delete(self, request, diagnostic_id):

        persons = list(PatientDiagnostic.objects.filter(
            diagnostic_id=diagnostic_id).values())

        if len(persons) > 0:

            PatientDiagnostic.objects.filter(
                diagnostic_id=diagnostic_id).delete()

            data = {'msg': 'deleted'}

        else:

            data = {'msg': 'not deleted'}

        return JsonResponse(data)


class vital_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, patient_id=0):

        if (patient_id > 0):

            vitals = list(VitalSigns.objects.filter(
                patient=patient_id).values())

            if len(vitals) > 0:

                vital = vitals[0]

                data = {'vitals': vital}

            else:

                data = {'msg': 'not found'}

            return JsonResponse(data)

        else:

            vitals = list(VitalSigns.objects.values())

            if len(vitals) > 0:

                data = {'vitals': vitals}

            else:

                data = {'message': 'not vitals registered'}

            return JsonResponse(data)

