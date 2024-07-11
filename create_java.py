#web 패키지 하위 클래스 생성
def create_controller_java(clazz_path, clazz_name):
    clazz_path_parts = '.'.join(clazz_path.replace('\\', '.').split('.'))
    package_path_index = clazz_path_parts.find('java.')
    package_path = clazz_path_parts[package_path_index + len('java.'):]
    module_path = '.'.join(package_path.split('.')[:-1])
    request_mapping_path_arr = package_path.replace('.', '/').split('/')
    request_mapping_path = '/'.join(request_mapping_path_arr[1:-1])

    #컨트롤러 클래스 작성
    controller_content = f"""package {package_path};


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import lombok.RequiredArgsConstructor;
import {module_path}.service.{clazz_name}Service;

@RequiredArgsConstructor
@RequestMapping("/{request_mapping_path}")
@Controller
public class {clazz_name}Controller {{

    private final {clazz_name}Service {clazz_name[0].lower() + clazz_name[1:]}Service;
}}
"""
    with open(clazz_path + '\\' + clazz_name + 'Controller.java', 'w') as controller_file:
        controller_file.write(controller_content)



#service 패키지 하위 클래스 생성
def create_service_java(clazz_path, clazz_name):
    clazz_path_parts = '.'.join(clazz_path.replace('\\', '.').split('.'))
    package_path_index = clazz_path_parts.find('java.')
    package_path = clazz_path_parts[package_path_index + len('java.'):]
    
    # 서비스 클래스 작성
    service_content = f"""package {package_path};
    

public interface {clazz_name}Service {{

}}
"""
    with open(clazz_path + '\\' + clazz_name + 'Service.java', 'w') as service_file:
        service_file.write(service_content)


    # VO 클래스 작성
    vo_content = f"""package {package_path};


import egovframework.com.cmm.CommonVO;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder(toBuilder = true)
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper=false)
public class {clazz_name}VO extends CommonVO {{


}}
"""

    with open(clazz_path + '\\' + clazz_name + 'VO.java', 'w') as vo_file:
        vo_file.write(vo_content)
    
    # VO 그룹 클래스 작성
    vo_group_content = f"""package {package_path};


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class {clazz_name} {{

    private {clazz_name}VO {clazz_name[0].lower() + clazz_name[1:]}VO;

    private List<{clazz_name}VO> {clazz_name[0].lower() + clazz_name[1:]}List;
}}
"""
    with open(clazz_path + '\\' + clazz_name + '.java', 'w') as vo_group_file:
        vo_group_file.write(vo_group_content)



#impl 패키지 하위 클래스 생성
def create_serviceImpl_java(clazz_path, clazz_name):
    clazz_path_parts = '.'.join(clazz_path.replace('\\', '.').split('.'))
    package_path_index = clazz_path_parts.find('java.')
    package_path = clazz_path_parts[package_path_index + len('java.'):]

    #serviceImpl 클래스 작성
    serviceImpl_content = f"""package {package_path};


import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import {'.'.join(package_path.split('.')[:-1])}.{clazz_name}Service;

@RequiredArgsConstructor
@Service("{clazz_name[0].lower() + clazz_name[1:]}Service")
public class {clazz_name}ServiceImpl implements {clazz_name}Service {{

    private final {clazz_name}DAO {clazz_name[0].lower() + clazz_name[1:]}DAO;
}}
"""
    with open(clazz_path + '\\' + clazz_name + 'ServiceImpl.java', 'w') as ServiceImpl_file:
        ServiceImpl_file.write(serviceImpl_content)

    #dao 클래스 작성
    dao_content = f"""package {package_path};


import egovframework.com.cmm.service.impl.EgovComAbstractDAO;
import org.springframework.stereotype.Repository;

@Repository("{clazz_name[0].lower() + clazz_name[1:]}DAO")
public class {clazz_name}DAO extends EgovComAbstractDAO {{

}}
"""
    with open(clazz_path + '\\' + clazz_name + 'DAO.java', 'w') as dao_file:
        dao_file.write(dao_content)